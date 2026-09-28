---
format: 1080x1920
duration: 30s
message: "Hari Romeow adalah siklus lucu yang berulang tanpa henti — tidur, minta makan, zoomies, bikin ulah, lalu tidur lagi"
arc: Judul buku → 7 fase siklus (tiap fase = satu lelucon + satu fakta) → kembali ke fase ① (loop)
audience: penonton Reels/TikTok/Shorts, pecinta kucing
mode: collaborative
version: v2
---

# Siklus Hidup Romeow — storyboard v2

## Keputusan

- **Pesan:** Hari Romeow adalah siklus lucu yang berulang tanpa henti.
- **Penonton dan alur:** pecinta kucing di feed vertikal. Judul buku → 7 fase → loop kembali ke ①.
- **Format:** 1080×1920, 30 detik, tanpa narasi, dengan musik latar dan efek suara. Semua teks penting berada di area aman (atas ±12% dan bawah ±20% dikosongkan untuk UI Reels/TikTok).
- **Romeow = satu aktor yang sama sepanjang video.** Romeow tidak digambar ulang per frame. Ia satu karakter di satu dunia pop-up, dengan ukuran tetap di semua close-up (kepala ±240px). Ia selalu berpijak di "rel" panah siklus, dan berjalan, melompat, atau berlari ke fase berikutnya **di dalam transisi**. Pose akhir di satu fase adalah pose awal di fase berikutnya.
- **Transisi 3D:** kamera perspektif sungguhan terbang di atas halaman pop-up (rotateX/rotateY/translateZ, parallax antar-lapis, blur kedalaman). Saat kamera pergi, potongan kertas fase lama **terlipat rebah** ke halaman, dan potongan fase baru **berdiri** seperti buku pop-up. Tiap sambungan punya gerak kamera sendiri supaya tidak berulang (lihat peta sambungan).
- **Tipografi menyatu dengan Romeow:** tidak ada lagi blok judul di atas. Kata-kata mengisi ruang kosong di sekitar Romeow dan bereaksi terhadapnya: melengkung di atas punggungnya, keluar dari mulutnya, jadi jejak lari, tercetak di kardus, jatuh bersama gelas. Hanya folio kecil "GBR. 1.3 · FASE n/7" yang tetap di pojok.
- **Benang merah (spine):** satu halaman buku pop-up *"Gambar 1.3"* dan **panah siklus biru** yang melingkar. Di setiap fase, sapuan stabilo kuning berjalan di potongan panah menuju fase berikutnya ("kamu di sini"). Romeow selalu berpindah fase mengikuti panah itu. Di penutup, stabilo melengkapi lingkaran lalu memudar, sehingga halaman kembali persis seperti detik 0.
- **Gaya 2.5D:** potongan kertas pada 3–4 lapis kedalaman (latar halaman, panggung properti, Romeow, label di depan), bayangan jatuh lembut, dan kamera CSS 3D yang bergeser di atas satu dunia pop-up.
- **Motion typography:**
  - label fase ditulis dengan serif display yang muncul huruf per huruf dengan pantulan pegas;
  - kata kunci diberi stabilo;
  - catatan fakta seperti ditulis tangan dan dicoret, dengan panah kecil tangan yang menunjuk ke objek.
- **Font:**
  - Fraunces (serif display, lembut) untuk judul dan label fase;
  - Caveat (tulisan tangan) untuk catatan fakta;
  - Space Mono untuk nomor gambar dan metadata ("Gbr. 1.3", "05:00").
  - Semua di-embed lewat `@font-face`.
- **Palet:**
  - latar: kertas `#F6F1E7`
  - teks dan garis: tinta `#2B4C7E`
  - aksen tunggal: stabilo kuning `#F7D154`
  - Romeow: abu `#8A9099` dan `#5E646C`, putih `#F7F7F5`, hidung `#F4B6C2`, mata `#8DBF6A`
- **Larangan:**
  - tidak ada kartu slideshow (setiap fase adalah tempat di halaman yang sama, bukan kartu baru);
  - tidak ada glow neon atau gradien;
  - tidak ada teks di bawah 32px;
  - tidak ada gerak "screensaver" yang tidak menyampaikan apa-apa;
  - tidak memakai foto kucing asli.
- **Frame diam (held frame):** fase ⑥, tepat setelah gelas jatuh. Romeow menatap kamera tanpa bergerak selama ±0,8 detik.
- **Aturan arah:** kamera selalu bergerak **searah jarum jam** mengikuti panah siklus.
- **Timing manual:** Romeow dan dunia pop-up adalah satu lapisan tetap. Tiap fase adalah klip sendiri di timeline Studio (tipografi dan properti fase). Kamera dan perjalanan Romeow dihitung dari batas klip-klip fase itu, jadi saat Anda menggeser atau memotong klip, transisi 3D ikut menyesuaikan.

## Changes from v1

- Rencana v1 disetujui pengguna tanpa perubahan. Sketsa v1 dibuat di `storyboard.html`.
- Catatan pengguna atas sketsa v1 (verbatim): "saya mau kucingnya dari frame ke frame itu continue kucing yang sama, lalu ada efek 3D juga ketika transisi.. lalu text typografinya jangan cuma diatas, tapi dia bisa kreatif menyatu dengan romeow mengisi breathed space"
- v2: Romeow jadi satu aktor kontinu (ukuran tetap, berpijak di rel panah, berpindah fase di dalam transisi). Transisi 3D berupa kamera terbang dengan potongan kertas yang terlipat dan berdiri. Tipografi dipindah dari blok atas ke ruang kosong di sekitar Romeow, di semua frame.

## Still open

- Bentuk telinga dan ekor Romeow dikunci di sketsa.
- Pilihan musik latar ditentukan saat build.

## Frame 1 — Pembuka: Buku Terbuka

- status: built
- src: compositions/01-pembuka.html
- duration: 3s
- transition_in: cut
- scene: Diagram pop-up utuh dari sudut miring 3D; "Siklus Hidup Romeow" ditulis DI DALAM lingkaran siklus; Romeow tidur di atas ①; keterangan gambar ala buku di bawah
- voiceover: onscreen
- blueprint: zoom-out-workspace-reveal (dibalik jadi pop-up berdiri lalu kamera turun) + rules: 3d-camera-flight, svg-path-draw, waterfall-entry
- hero_prop: panah siklus (callback di Frame 9)
- audio: kertas "fwup" kecil di 0.3s, musik mulai
- constraint: tidak ada logo atau kartu judul terpisah; judul adalah bagian dari halaman buku

(00.0–03.0) Kamera memandang halaman pop-up dari atas dengan sudut miring, dan semua potongan kertas sudah berdiri. Supaya loop mulus, frame ini identik dengan frame terakhir. Gerak pertama terjadi dalam 0,2 detik: kata **"Romeow"** di judul memantul dan disapu stabilo kuning, tujuh nomor fase berdenyut bergiliran searah jarum jam, dan potongan kertas bergoyang pelan. Kamera lalu meluncur turun mendekat ke ①, tempat Romeow meringkuk.
**Kenapa:** memperkenalkan format parodi buku IPA sekaligus menjanjikan sebuah "siklus".

## Frame 2 — ① Hibernasi Harian

- status: built
- src: compositions/02-hibernasi.html
- duration: 3.5s
- transition_in: 3d-dive — kamera menukik dari sudut 35° ke ①, potongan fase ① berdiri
- scene: "Hibernasi Harian" melengkung di atas punggung Romeow seperti selimut; rantai Z keluar dari hidungnya dan berubah jadi "12–16 jam sehari" di ruang kosong atas
- voiceover: onscreen
- rules: sine-wave-loop (napas), spring-pop-entrance (label), css-marker-patterns (stabilo "12–16 jam")
- audio: dengkur lembut
- constraint: tidak ada ikon bulan dan bintang klise

(03.0–06.5) Close-up Romeow dengan dada naik turun. Huruf "z" kertas melayang ke atas dengan jarak kedalaman yang berbeda-beda. Label fase muncul memantul huruf per huruf. Catatan tulisan tangan *"tidur 12–16 jam sehari"* tertulis, lalu "12–16 jam" disapu stabilo kuning.
**Kenapa:** membuka siklus dengan fase terpanjang, yaitu fakta pertama.

## Frame 3 — ② Peregangan Ekstrem

- status: built
- src: compositions/03-peregangan.html
- duration: 3s
- transition_in: 3d-orbit-glide — kamera mengorbit sepanjang busur, Romeow bangun dan berjalan
- scene: Romeow meregang diagonal; "Peregangan" dan "EKSTREM" sejajar garis punggungnya dan ikut meregang; fakta di bawah perut
- voiceover: onscreen
- rules: press-release-spring (regang lalu kembali), kinetic-beat-slam (kata "EKSTREM" meregang ikut badan)
- audio: "nyaaawn" menguap
- constraint: Romeow tidak boleh berubah bentuk jadi karet tanpa batas; batas regang maksimal 1.6×

(06.5–09.5) Kamera bergeser searah jarum jam. Romeow meregang panjang, dan kata **"EKSTREM"** ikut meregang secara horizontal mengikuti badannya. Setelah itu keduanya kembali ke bentuk semula dengan pantulan pegas.
**Kenapa:** tipografi kinetik yang meniru gerak kucing adalah lelucon visual utama fase ini.

## Frame 4 — ③ Alarm Jam 05.00

- status: built
- src: compositions/04-alarm.html
- duration: 3.5s
- transition_in: 3d-hop — Romeow melompat, kamera ikut naik (rotateX) lalu turun
- scene: "MEOW" menyembur dari mulut Romeow tiga kali, makin besar, ke arah jam; "05.00" tertulis di muka jam; "ALARM JAM" melingkar di bingkai jam
- voiceover: onscreen
- rules: counting-dynamic-scale (MEOW makin besar), vertical-spring-ticker (angka jam bergulir ke 05:00)
- audio: meow ×3 makin keras
- constraint: tidak ada gambar manusia; "korban" cukup diwakili bantal kertas yang bergetar

(09.5–13.0) Angka jam bergulir ke **05:00**. Balon **"MEOW!"** muncul tiga kali, dan setiap kali ukurannya membesar dan bergetar. Pada kali ketiga, balon memenuhi setengah frame.
**Kenapa:** fase yang paling dikenali pemilik kucing.

## Frame 5 — ④ Makan 3 Suap

- status: built
- src: compositions/05-makan.html
- duration: 3.5s
- transition_in: 3d-whip-orbit — kamera berayun cepat dengan blur kedalaman, Romeow berlari kecil ke mangkuk
- scene: Angka "3" raksasa kuning berdiri di belakang Romeow sebagai lapisan pop-up; "Makan" dan "Suap" mengapitnya; huruf "kriuk" terlempar dari mangkuk; "sisa: 97%" di mangkuk
- voiceover: onscreen
- rules: counting-dynamic-scale (100% → 97%), spring-pop-entrance
- audio: kriuk ×3
- constraint: angka hanya berkurang 3%, tidak lebih; lelucon ada di kecilnya angka itu

(13.0–16.5) Setiap kali Romeow mengunyah, angka di mangkuk turun: 100% → 99% → 98% → **97%**. Romeow lalu berbalik pergi dengan ekor terangkat. Label *"sisa: 97%"* diberi lingkaran tangan.
**Kenapa:** angka yang turun sedikit sekali adalah punchline-nya.

## Frame 6 — ⑤ Zoomies

- status: built
- src: compositions/06-zoomies.html
- duration: 3.5s
- transition_in: 3d-spin — kamera berputar mengelilingi pusat lingkaran, Romeow melesat dengan motion blur
- scene: Huruf Z-O-O-M-I-E-S jadi jejak lari Romeow di sepanjang rel, makin pudar dan meregang ke belakang; halaman miring 3D
- voiceover: onscreen
- rules: motion-blur-streak, 3d-camera-flight (putaran kamera), kinetic-beat-slam (ZOOMIES menghantam masuk)
- audio: whoosh ×2, rem "skrrt"
- constraint: putaran kamera maksimal 1 kali; tidak boleh ada flash atau strobo

(16.5–20.0) Satu-satunya fase dengan kamera cepat. Romeow melesat mengikuti panah dengan motion blur dan kamera ikut berputar. Tiba-tiba ia berhenti diam, dan kata **"ZOOMIES"** menghantam masuk dari samping.
**Kenapa:** puncak energi di tengah video; ritmenya kontras dengan fase-fase yang pelan.

## Frame 7 — ⑥ Eksperimen Gravitasi

- status: built
- src: compositions/07-gravitasi.html
- duration: 3.5s
- transition_in: 3d-crash-low — rem mendadak, kamera turun ke sudut rendah sejajar mata Romeow
- scene: "Eksperimen" di ruang kosong atas; huruf G-R-A-V-I-T-A-S-I jatuh berputar mengikuti lintasan gelas; Romeow menatap kamera; frame diam
- voiceover: onscreen
- rules: nudge-curve (dorongan pelan-pelan), depth-of-field-blur (fokus ke mata Romeow)
- audio: geser gelas, "tink!", lalu hening 0.8s
- constraint: tidak ada pecahan yang dramatis; cukup "tink" dan bintang kecil

(20.0–23.5) Gelas didorong sedikit demi sedikit ke tepi meja sementara mata Romeow menatap lurus ke kamera. Gelas jatuh ke luar frame, lalu terdengar "tink!". **Frame diam:** Romeow tetap menatap tanpa bergerak selama 0,8 detik. Setelah itu label dan catatan muncul.
**Kenapa:** frame diam ini adalah titik komedi paling kuat di video.

## Frame 8 — ⑦ Masuk Kardus

- status: built
- src: compositions/08-kardus.html
- duration: 3.5s
- transition_in: 3d-tilt-follow — kamera mengikuti gelas jatuh (miring ke bawah), mendarat di kardus
- scene: "KARDUS" tercetak di muka kardus seperti cap pengiriman; panah tulisan tangan "masuk ↓"; label "ISI: 1 KUCING (TERLALU BESAR)"; fakta di label gantung
- voiceover: onscreen
- rules: press-release-spring (kardus melentur saat dimasuki), spring-pop-entrance
- audio: "pluk"
- constraint: kardus harus jelas lebih kecil dari Romeow

(23.5–27.0) Romeow melompat masuk kardus. Kardus melentur, lalu bulu surai dan ekornya menyembul ke segala arah. Hanya kepalanya yang terlihat, dan ia tampak puas.
**Kenapa:** lelucon terakhir sebelum siklus kembali.

## Frame 9 — Penutup: Kembali ke ①

- status: built
- src: compositions/09-penutup.html
- duration: 3s
- transition_in: 3d-pull-up — kamera naik dan miring ke pandangan halaman penuh
- scene: Kamera naik dan miring kembali ke pandangan 3D penuh; stabilo menutup lingkaran; Romeow berjalan di rel kembali ke ① dan meringkuk — frame akhir = frame awal
- voiceover: onscreen
- blueprint: zoom-out-workspace-reveal + rules: viewport-change (kamera mundur), css-marker-patterns (stabilo menutup lingkaran)
- hero_prop: panah siklus menutup (callback dari Frame 1)
- audio: dengkur + musik selesai tepat di akhir bar
- constraint: pose kamera dan elemen di 30.0s harus identik dengan 0.0s

(27.0–30.0) Kamera mundur ke pandangan halaman penuh. Stabilo menyapu potongan panah terakhir sehingga lingkarannya lengkap, lalu seluruh stabilo memudar. Romeow berjalan ke ① dan meringkuk lagi. Kondisi di detik terakhir sama persis dengan pose di detik 0.
**Kenapa:** membayar janji "siklus" di Frame 1 dan membuat video bisa diputar berulang tanpa sambungan.
