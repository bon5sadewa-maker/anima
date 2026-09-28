#!/usr/bin/env python3
"""Build compositions/world.html from src/world.src.html.

Inlines Romeow's drawing library (from storyboard.html, so the character stays
identical to the locked sketches), the floor diagram and the seven pop-up pages.
Props are positioned so they land exactly where the sketches put them when the
camera sits on their page (screen = page coords for z = 0; deeper layers are
pre-scaled by (P - z) / P).
"""
import math
import pathlib

ROOT = pathlib.Path(__file__).parent
P, RP, RR, N = 1800, 1140, 980, 7
STEP = 360 / N
INK, HI, PAPER = "#2B4C7E", "#F7D154", "#F6F1E7"
LABELS = ["Hibernasi", "Peregangan", "Alarm 05.00", "Makan", "Zoomies", "Gravitasi", "Kardus"]


def romeow_defs():
    s = (ROOT / "storyboard.html").read_text()
    a = s.index('<g id="rm-ear">')
    b = s.index('<g id="folio">')
    speed_a = s.index('<path id="speed"')
    speed_b = s.index("\n", speed_a)
    return s[a:b] + s[speed_a:speed_b]


def place(sx, sy_bottom, z, w, h, cls, pid, inner, viewbox=None, extra=""):
    """Position a prop so it appears at screen (sx centre, sy_bottom) with apparent size w x h."""
    k = (P - z) / P
    cx = 540 + (sx - 540) * k
    by = 960 + (sy_bottom - 960) * k
    pw, ph = w * k, h * k
    vb = viewbox or f"0 0 {w} {h}"
    return (
        f'<div class="w-prop {cls}" id="{pid}" data-z="{z}" data-layout-ignore '
        f'style="left:{cx - pw / 2:.1f}px;top:{by - ph:.1f}px;width:{pw:.1f}px;height:{ph:.1f}px"{extra}>'
        f'<svg viewBox="{vb}">{inner}</svg></div>'
    )


def floor_y(z):
    """Screen y where the floor meets depth z (for props standing on the floor)."""
    return 960 + 340 * P / (P - z)


def props(k):
    out = []
    if k == 3:  # alarm: wall clock + pillow on the floor
        out.append(place(850, 450 + 150, 40, 300, 300, "", "w-clock",
            f'<circle cx="150" cy="150" r="138" fill="#FFFDF7" stroke="{INK}" stroke-width="9"/>'
            f'<path d="M150,30 v24 M150,246 v24 M30,150 h24 M246,150 h24" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
            extra=' filter-cut="1"'))
        out.append(place(800, floor_y(280), 280, 290, 130, "", "w-pillow",
            f'<g filter="url(#w-cut)"><rect x="10" y="20" width="270" height="100" rx="46" fill="#FFFDF7" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M60,70 q30,-14 60,0 q30,14 60,0" stroke="{INK}" stroke-width="4" fill="none" opacity="0.4"/></g>'))
    if k == 4:  # makan: giant yellow 3 (back layer) + bowl (front layer)
        out.append(place(450, floor_y(20), 20, 620, 860, "", "w-three",
            f'<g filter="url(#w-cut)"><text x="310" y="790" font-family="Fraunces" font-weight="900" font-size="1000" fill="{HI}" text-anchor="middle">3</text></g>',
            viewbox="0 0 620 860"))
        out.append(place(750, floor_y(280), 280, 440, 170, "", "w-bowl",
            f'<g filter="url(#w-cut)"><path d="M10,40 H430 L395,165 H45 Z" fill="#FFFDF7" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
            f'<path d="M30,40 q40,-50 80,-10 q30,-50 70,-6 q30,-48 70,-4 q40,-46 80,-2 q40,-40 70,22" fill="#C99E6B"/></g>',
            viewbox="0 -30 440 200"))
    if k == 5:  # zoomies: paper speed strips at two depths
        out.append(place(330, 1000, 60, 560, 260, "w-speed", "w-speed-a", '<use href="#speed" transform="scale(1.6 1)"/>', viewbox="0 -10 560 260"))
        out.append(place(420, 1240, 320, 520, 200, "w-speed", "w-speed-b", '<use href="#speed" transform="scale(1.5 0.8)"/>', viewbox="0 -10 520 200"))
    if k == 6:  # gravitasi: table + glass
        top = 930
        out.append(place(700, floor_y(90), 90, 440, floor_y(90) - top, "", "w-table",
            f'<g filter="url(#w-cut)"><rect x="10" y="4" width="420" height="36" rx="8" fill="#FFFDF7" stroke="{INK}" stroke-width="7"/>'
            f'<rect x="40" y="40" width="26" height="{floor_y(90) - top - 44:.0f}" fill="#FFFDF7" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="374" y="40" width="26" height="{floor_y(90) - top - 44:.0f}" fill="#FFFDF7" stroke="{INK}" stroke-width="6"/></g>',
            viewbox=f"0 0 440 {floor_y(90) - top:.0f}"))
        out.append(place(650, top + 6, 95, 90, 130, "", "w-glass",
            f'<g filter="url(#w-cut)"><path d="M5,5 h80 l-10,120 h-60 Z" fill="#DCE6F2" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M14,40 h62" stroke="{INK}" stroke-width="3" opacity="0.4"/></g>',
            viewbox="0 0 90 130"))
    if k == 7:  # kardus: back flap behind Romeow, box front in front of him
        out.append(place(545, floor_y(120) - 230, 120, 470, 110, "", "w-flap",
            '<path d="M0,110 L60,0 H400 L470,110 Z" fill="#B88A58"/>', viewbox="0 0 470 110"))
        out.append(place(545, floor_y(260), 260, 560, 280, "", "w-box",
            '<g filter="url(#w-cut)"><rect x="55" y="30" width="450" height="250" fill="#C99E6B" stroke="#8E6A40" stroke-width="6"/>'
            '<path d="M55,30 L0,110 H55 Z M505,30 L560,110 H505 Z" fill="#B88A58"/></g>',
            viewbox="0 0 560 280"))
    return "".join(out)


FRONT_Z = 200  # props deeper than this stand in front of Romeow (z 160) -> rig C


def split_props(k):
    back, front = [], []
    for chunk in props(k).split('<div class="w-prop')[1:]:
        html = '<div class="w-prop' + chunk
        z = float(html.split('data-z="')[1].split('"')[0])
        (front if z > FRONT_Z else back).append(html)
    return "".join(back), "".join(front)


def pages():
    out = []
    for k in range(1, N + 1):
        a = -(k - 1) * STEP
        back, _ = split_props(k)
        out.append(
            f'<div class="w-pagepos" data-k="{k}" id="w-page-{k}" style="transform: rotateY({a:.4f}deg) translateZ({RP}px) rotateY(180deg)">'
            f'<div class="w-pagefold" data-k="{k}" id="w-pagefold-{k}">'
            f'<div class="w-face w-front"><div class="w-paper"></div>{back}</div>'
            f'<div class="w-face w-back" style="transform: rotateY(180deg)"><div class="w-paper"></div><div class="w-backnum" data-layout-ignore>{k}</div></div>'
            f"</div></div>"
        )
    return "\n".join(out)


def fg_pages():
    out = []
    for k in range(1, N + 1):
        _, front = split_props(k)
        if not front:
            continue
        a = -(k - 1) * STEP
        out.append(
            f'<div class="w-pagepos" data-k="{k}" style="transform: rotateY({a:.4f}deg) translateZ({RP}px) rotateY(180deg)">'
            f'<div class="w-pagefold" data-k="{k}"><div class="w-face">{front}</div></div></div>'
        )
    return "\n".join(out)


def diagram_art():
    """The textbook diagram drawn on the floor (shared by all 7 wedges via <use>)."""
    F = 1300
    parts = ['<g id="w-art">']
    parts.append(f'<rect x="{-F}" y="{-F}" width="{2 * F}" height="{2 * F}" fill="#F2EBDD"/>')
    parts.append(f'<rect x="{-F}" y="{-F}" width="{2 * F}" height="{2 * F}" fill="url(#w-rule)"/>')
    circ = 2 * math.pi * RR
    parts.append(
        f'<circle id="w-ringhi" cx="0" cy="0" r="{RR}" fill="none" stroke="{HI}" stroke-width="64" '
        f'stroke-dasharray="0 {circ:.1f}" transform="rotate(90)" stroke-linecap="round"/>'
    )
    parts.append(f'<circle cx="0" cy="0" r="{RR}" fill="none" stroke="{INK}" stroke-width="12"/>')
    for k in range(N):
        am = math.radians(-(k * STEP + STEP / 2))
        x, y = RR * math.sin(am), RR * math.cos(am)
        rot = -math.degrees(am) + 180
        parts.append(f'<path d="M-40,-34 L40,0 L-40,34 Z" fill="{INK}" transform="translate({x:.1f} {y:.1f}) rotate({rot:.2f})"/>')
    parts.append('<g id="w-diagram">')
    for k in range(1, N + 1):
        a = math.radians(-(k - 1) * STEP)
        x, y = RR * math.sin(a), RR * math.cos(a)
        if k == 1:
            x, y = x + 360, y - 60
        parts.append(
            f'<g transform="translate({x:.1f} {y:.1f}) rotate(180)">'
            f'<circle r="120" fill="{"#2B4C7E" if k == 1 else "#FFFDF7"}" stroke="{INK}" stroke-width="12"/>'
            f'<text y="52" font-family="Fraunces" font-weight="900" font-size="150" text-anchor="middle" fill="{"#F6F1E7" if k == 1 else INK}">{k}</text></g>'
        )
        lx, ly = (RR - 300) * math.sin(a), (RR - 300) * math.cos(a)
        if k == 1:
            lx, ly = 0, RR - 420
        parts.append(
            f'<text transform="translate({lx:.1f} {ly:.1f}) rotate(180)" font-family="Fraunces" font-weight="700" font-size="96" '
            f'text-anchor="middle" fill="{INK}" stroke="#F2EBDD" stroke-width="24" paint-order="stroke" stroke-linejoin="round">{LABELS[k - 1]}</text>'
        )
    parts.append(
        '<g transform="rotate(180)">'
        f'<text x="0" y="-150" font-family="Fraunces" font-weight="900" font-size="190" text-anchor="middle" fill="{INK}">Siklus Hidup</text>'
        f'<rect id="w-title-hi" x="-620" y="-40" width="1240" height="270" fill="{HI}" transform="rotate(-2)"/>'
        f'<text id="w-title-romeow" x="0" y="190" font-family="Fraunces" font-weight="900" font-size="300" text-anchor="middle" fill="{INK}">Romeow</text>'
        "</g>"
    )
    parts.append("</g></g>")
    parts.append(
        '<pattern id="w-rule" width="120" height="120" patternUnits="userSpaceOnUse">'
        f'<line x1="0" y1="119" x2="120" y2="119" stroke="{INK}" stroke-opacity="0.07" stroke-width="3"/></pattern>'
    )
    return "".join(parts)


def wedges():
    """Floor = 7 triangles (centre -> page k's base). Each element box is only as big as its
    triangle, so a hidden-or-not wedge never has geometry behind the lens."""
    half = RP * math.tan(math.radians(STEP / 2)) + 8
    W, H = 2 * half, RP + 6
    out = []
    for k in range(1, N + 1):
        a = -(k - 1) * STEP
        poly = f"0,0 {-half:.1f},{H:.1f} {half:.1f},{H:.1f}"
        out.append(
            f'<div class="w-wedgepos" data-layout-ignore style="transform: rotateY({a:.4f}deg)">'
            f'<div class="w-wedge" id="w-wedge-{k}" style="left:{-half:.1f}px;width:{W:.1f}px;height:{H:.1f}px">'
            f'<svg viewBox="{-half:.1f} 0 {W:.1f} {H:.1f}">'
            f'<clipPath id="w-clip-{k}"><polygon points="{poly}"/></clipPath>'
            f'<g clip-path="url(#w-clip-{k})"><use href="#w-art" transform="rotate({a:.4f})"/></g></svg></div></div>'
        )
    return "\n".join(out)


def main():
    src = (ROOT / "src" / "world.src.html").read_text()
    out = src.replace("%%DEFS%%", romeow_defs() + diagram_art()).replace("%%FLOOR%%", wedges()).replace("%%PAGES%%", pages()).replace("%%FGPAGES%%", fg_pages())
    assert f"translateZ({RR}px)" in out, "keep #w-rad's CSS radius in sync with RR"
    (ROOT / "compositions" / "world.html").write_text(out)
    print("wrote compositions/world.html", len(out))


if __name__ == "__main__":
    main()
