#!/usr/bin/env python3
"""Offline music bed for Siklus Hidup Romeow: ukulele strums + pizzicato, 128 BPM.

16 bars x 1.875 s = exactly 30 s. Note tails that ring past the end are wrapped
back onto the start, so the file loops with no seam (the video loops too).
Pure Python (Karplus-Strong plucked strings), deterministic seed.

    python3 src/compose-bgm.py  ->  assets/audio/romeow-bgm.wav
"""
import array
import math
import pathlib
import random
import struct
import wave

SR = 44100
BPM = 128
BEAT = 60 / BPM
BAR = 4 * BEAT
BARS = 16
LEN = int(round(BARS * BAR * SR))  # 30 s
TAIL = int(3 * SR)
rng = random.Random(1307)

L = array.array("d", [0.0]) * (LEN + TAIL)
R = array.array("d", [0.0]) * (LEN + TAIL)

NOTE = {}
for name, semis in [("C", -9), ("D", -7), ("E", -5), ("F", -4), ("G", -2), ("A", 0), ("B", 2)]:
    for octave in range(1, 7):
        NOTE[f"{name}{octave}"] = 440 * 2 ** ((semis + 12 * (octave - 4)) / 12)


def pluck(freq, start, dur, gain, pan, decay=0.996, bright=0.5):
    """Karplus-Strong string, mixed into L/R at `start` seconds."""
    n = int(dur * SR)
    period = max(2, int(SR / freq))
    buf = [rng.uniform(-1, 1) for _ in range(period)]
    # soften the attack for the ukulele (bright < 1 -> darker pick)
    for i in range(1, period):
        buf[i] = bright * buf[i] + (1 - bright) * buf[i - 1]
    s0 = int(start * SR)
    gl = gain * math.cos(pan * math.pi / 2)
    gr = gain * math.sin(pan * math.pi / 2)
    idx = 0
    prev = 0.0
    for k in range(n):
        cur = buf[idx]
        nxt = buf[(idx + 1) % period]
        v = decay * 0.5 * (cur + nxt)
        buf[idx] = v
        idx = (idx + 1) % period
        # tiny DC blocker keeps the mix centred
        out = cur - prev * 0.995
        prev = cur
        j = s0 + k
        if j >= LEN + TAIL:
            break
        env = 1.0 if k > 60 else k / 60  # 1.4 ms click guard
        L[j] += out * gl * env
        R[j] += out * gr * env


UKE = {
    "C": ["G4", "C4", "E4", "C5"],
    "Am": ["A4", "C4", "E4", "A4"],
    "F": ["A4", "C4", "F4", "A4"],
    "G": ["G4", "D4", "G4", "B4"],
    "Em": ["G4", "E4", "G4", "B4"],
}
BASS = {"C": "C3", "Am": "A2", "F": "F2", "G": "G2", "Em": "E2"}
PROG = ["C", "Am", "F", "G", "C", "Am", "F", "G", "F", "G", "Em", "Am", "F", "G", "C", "C"]
# strum on these eighths: (eighth index, direction, accent)
STRUM = [(0, "d", 1.0), (2, "d", 0.7), (3, "u", 0.55), (5, "u", 0.6), (6, "d", 0.8), (7, "u", 0.5)]

MEL = [
    "E5 - G5 - A5 G5 E5 -", "C5 - D5 E5 - - - -",
    "F5 - A5 - C6 A5 F5 -", "G5 - F5 D5 - B4 - -",
    "E5 - G5 - A5 G5 E5 -", "C5 - D5 E5 - - - -",
    "F5 - A5 - C6 A5 F5 -", "G5 - - - - - - -",
    "A5 - C6 - A5 - F5 -", "G5 - B5 - D6 - B5 -",
    "G5 - E5 - B4 - E5 -", "A5 - - E5 - C5 - -",
    "F5 - A5 C6 - A5 - F5", "D5 - G5 B5 - G5 - D5",
    "E5 - G5 - C6 - - -", "- - - - - - - -",
]

for bar, chord in enumerate(PROG):
    t0 = bar * BAR
    # ukulele strums (left of centre)
    for eighth, direction, accent in STRUM:
        strings = UKE[chord] if direction == "d" else list(reversed(UKE[chord]))
        for si, note in enumerate(strings):
            pluck(NOTE[note], t0 + eighth * BEAT / 2 + si * 0.011, 1.1, 0.16 * accent, 0.3, decay=0.9955, bright=0.45)
    # pizzicato bass on beats 1 and 3 (centre)
    for beat in (0, 2):
        pluck(NOTE[BASS[chord]], t0 + beat * BEAT, 0.7, 0.42, 0.5, decay=0.989, bright=0.35)
    # pizzicato melody (right of centre), short and dry
    for eighth, tok in enumerate(MEL[bar].split()):
        if tok != "-":
            pluck(NOTE[tok], t0 + eighth * BEAT / 2, 0.45, 0.26, 0.72, decay=0.982, bright=0.7)
    # soft shaker on the off-beats
    for eighth in (1, 3, 5, 7):
        s = int((t0 + eighth * BEAT / 2) * SR)
        last = 0.0
        for k in range(int(0.045 * SR)):
            noise = rng.uniform(-1, 1)
            hp = noise - last
            last = noise
            env = math.exp(-k / (0.012 * SR))
            L[s + k] += hp * 0.018 * env
            R[s + k] += hp * 0.022 * env

# wrap the ringing tails onto the start -> seamless loop
for k in range(TAIL):
    L[k] += L[LEN + k]
    R[k] += R[LEN + k]

# gentle tanh limiter: plucks are very peaky, lift the body of the bed (~+10 dB)
peak = max(max(abs(v) for v in L[:LEN]), max(abs(v) for v in R[:LEN]))
drive = 3.2 / peak
for i in range(LEN):
    L[i] = math.tanh(L[i] * drive)
    R[i] = math.tanh(R[i] * drive)
peak = max(max(abs(v) for v in L[:LEN]), max(abs(v) for v in R[:LEN]))
g = (10 ** (-3 / 20)) / peak
out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "audio" / "romeow-bgm.wav"
out.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(out), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    frames = bytearray()
    for i in range(LEN):
        frames += struct.pack("<hh", int(max(-1, min(1, L[i] * g)) * 32767), int(max(-1, min(1, R[i] * g)) * 32767))
    w.writeframes(bytes(frames))
print(f"wrote {out} ({LEN / SR:.3f} s, peak gain {g:.3f})")
