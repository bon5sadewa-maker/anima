---
workflow: general-video
flow: companion
storyboard: yes
message: "Hari Romeow adalah siklus lucu yang berulang tanpa henti — tidur, minta makan, zoomies, bikin ulah, lalu tidur lagi"
destination: reels-tiktok-shorts
aspect: 1080x1920
language: id
length: 30s
angle: concept
---

## Intent

Motion explainer 30 detik, loop mulus, tentang siklus kegiatan harian kucing rumah
yang lucu menggemaskan. Konsep terpilih: **"Siklus Kucing" — parodi diagram "Siklus Air"
buku IPA SD**. Tujuh fase dihubungkan panah melingkar, tiap fase diberi label ilmiah
yang sok serius, plus satu catatan fakta pendek. Lucunya datang dari kontras antara
gaya ilmiah yang serius dan kelakuan kucing yang absurd.

Judul: *"Gambar 1.3 — Siklus Hidup Romeow"*.

Fase (0–30s): Pembuka (0–3) → ① Hibernasi Harian (3–6.5) → ② Peregangan Ekstrem
(6.5–9.5) → ③ Alarm Jam 05.00 (9.5–13) → ④ Makan 3 Suap (13–16.5) → ⑤ Zoomies
(16.5–20) → ⑥ Eksperimen Gravitasi (20–23.5) → ⑦ Masuk Kardus (23.5–27) →
Penutup, kembali ke ① (27–30). Frame 30s = frame 0.

## Assets

- (belum ada file) — Karakter: **Romeow**, kucing abu-abu, mulut/dagu putih, ras mix
  Norwegian Forest (surai leher lebat, ujung telinga berjumbai, ekor sangat mengembang).
  Digambar sebagai ilustrasi potongan kertas.

## Customizations

- **2.5D experience** — buku pop-up: halaman buku pelajaran terbuka, elemen berupa potongan
  kertas berdiri di kedalaman berbeda dengan bayangan lembut; kamera bergerak dengan parallax.
- **Motion typography** — label fase dan catatan fakta tampil sebagai tipografi kinetik
  (bukan teks statis).
- **Catatan fakta** per fase, gaya tulisan tangan.
- **Timing bisa direvisi manual** — tiap fase adalah klip/sub-komposisi terpisah di timeline
  HyperFrames Studio, animasi di dalamnya relatif terhadap awal klip.
- **Audio**: tanpa narasi; musik latar ukulele/pizzicato ringan yang bisa di-loop + SFX per
  fase (dengkur, meow, kriuk ×3, whoosh, tink gelas, pluk kardus).

## Notes

- 9:16: kamera mendekat ke tiap fase supaya label terbaca di HP; diagram utuh hanya di
  pembuka dan penutup.
- Loop harus mulus: frame terakhir identik dengan frame pertama.
- Palet awal: kertas krem `#F6F1E7`, tinta biru `#2B4C7E`, abu Romeow `#8A9099` / `#5E646C`,
  putih mulut `#F7F7F5`, hidung pink `#F4B6C2`, mata hijau `#8DBF6A`.
- Teknik: 3D berbasis CSS + GSAP (tanpa engine 3D penuh), render deterministik.
