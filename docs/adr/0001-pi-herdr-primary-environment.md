# Pi dan herdr sebagai environment utama

Fork ini menargetkan Pi sebagai koordinator dan worker, dengan herdr sebagai pengelola sesi terminal serta akses ke agent pada satu mesin. Pengguna harus dapat melihat dan mengintervensi pekerjaan worker tanpa wajib menyetujui setiap langkah.

Prinsip engineering dan playbook pstack yang masih berguna dipertahankan. Kompatibilitas penuh dengan Cursor dan Claude Code bukan kewajiban. Pilihan ini mengutamakan alur kerja pengguna daripada abstraksi lintas environment. Hermes bukan ketergantungan fork ini, dan koordinasi lintas mesin berada di luar tahap pertama.

## Delegasi dan isolasi

Hanya skill yang memang meminta subagent yang membuat worker Pi di herdr. Setiap worker tersebut harus terlihat dan dapat diintervensi pengguna. Skill lain tetap berjalan di koordinator tanpa kewajiban membuat worker.

Semua pembuatan worker menjadi tanggung jawab koordinator. Jika skill yang dijalankan worker membutuhkan worker tambahan, worker meminta delegasi tersebut kepada koordinator. Worker tidak membuat worker lain sendiri. Aturan ini menjaga agar koordinator mengetahui seluruh agent, tugas, dan lokasi kerjanya.

Setiap worker yang mengubah file mendapat branch dan worktree sendiri. Worker yang hanya membaca boleh memakai direktori yang sama. Koordinator memeriksa hasil sebelum mengintegrasikannya agar worker tidak saling menimpa perubahan.

Jika herdr tidak tersedia, delegasi berhenti dengan penjelasan. Koordinator boleh mengerjakan sendiri pekerjaan yang tidak memerlukan worker, tetapi harus menyatakan keterbatasan tersebut. Worker tersembunyi bukan fallback yang diizinkan.

Jika worker macet, statusnya tidak jelas, atau menunggu persetujuan, koordinator memeriksa status dan output sebelum bertindak. Koordinator tidak otomatis mengirim ulang prompt, menjawab persetujuan, atau memulai worker pengganti. Jika kondisi belum dapat dipastikan, koordinator melaporkan masalah dan menahan pekerjaan yang bergantung pada worker tersebut. Worker lain boleh melanjutkan pekerjaan.

## Batas otonomi

Secara default, agent boleh membaca, mengedit, menjalankan tes, membuat commit lokal, dan mengintegrasikan hasil lokal. Push, membuat PR atau MR, merge ke remote, deploy, dan tindakan destruktif memerlukan izin pengguna.

Pengguna dapat memberikan izin per tugas hingga pembuatan PR atau MR. Izin tersebut mencakup push branch yang diperlukan untuk pengajuan itu, tetapi tidak otomatis mencakup merge, deploy, force-push, atau tindakan destruktif.

## Pengambilalihan manual

Pengguna menyatakan pengambilalihan worker kepada koordinator. Koordinator berhenti mengirim tugas ke worker tersebut sampai pengguna mengembalikannya. Worker lain boleh melanjutkan pekerjaan. Tahap pertama tidak mengandalkan deteksi otomatis saat pengguna mengetik di pane.

## Eksekusi dan layout

Versi pertama memakai skill, dokumentasi, dan CLI bawaan herdr serta Pi. Tidak ada extension Pi, daemon, atau orchestration engine baru.

Koordinator boleh membuat tempat kerja worker secara otomatis tanpa memindahkan fokus pengguna, memakai ulang pane milik pengguna, atau merombak pane yang sudah ada. Koordinator mendapat area utama yang lebih besar, sedangkan worker memakai area lebih kecil. Jika pane worker sulit dibaca, worker tambahan ditempatkan di tab lain. Semua worker tetap dapat diakses melalui herdr.

Sesi worker yang selesai tetap terbuka sampai pengguna meminta pembersihan. Pane, branch, dan worktree tidak dihapus otomatis.

## Pengaturan dan cakupan

Alur setup pstack tetap menawarkan budget reasoning, mendeteksi model yang tersedia, dan meminta konfirmasi pemetaan model per peran. Budget bukan batas biaya uang. Eksekusi memakai identitas model dan tingkat reasoning yang didukung Pi. Jika pilihan tidak tersedia, setup menampilkan alternatif untuk dikonfirmasi, bukan mengganti model diam-diam.

Jumlah worker mengikuti kebutuhan skill dan konfigurasi panel tanpa batas paralelisme tambahan dari fork ini. Pekerjaan independen boleh berjalan bersamaan. Pekerjaan yang bergantung pada hasil sebelumnya tetap menunggu.

Penyesuaian berlaku di seluruh pstack, termasuk skill yang dipanggil langsung tanpa poteto-mode. Tujuan masing-masing skill dan prinsip engineering dipertahankan. Fitur khusus Cursor tanpa padanan dinyatakan tidak didukung dengan penjelasan. Fork ini tidak membangun pengganti Cursor Automations, Bugbot, atau paket automation Benny.

## Pembaruan upstream

Pembaruan upstream ditinjau dan diambil secara selektif, bukan disinkronkan otomatis sebagai mirror. Atribusi dan asal perubahan dipertahankan. Pilihan ini menghindari pembaruan upstream yang menimpa aturan Pi dan herdr.

## Kriteria penerimaan

Implementasi belum selesai hanya dengan memperbarui Markdown. Alur nyata Pi dan herdr harus diuji pada repo percobaan, dengan satu pemeriksaan yang dapat dijalankan ulang tanpa framework baru.

Pengujian mencakup:

- Pemanggilan skill langsung dan melalui poteto-mode.
- Worker pembaca serta worker penulis dengan branch dan worktree terpisah.
- Pengiriman tugas, pembacaan hasil, dan pemeriksaan hasil oleh koordinator.
- Permintaan delegasi tambahan dari worker yang hanya dijalankan oleh koordinator.
- Pengambilalihan manual tanpa pengiriman tugas baru oleh koordinator sampai kendali dikembalikan.
- Penanganan worker bermasalah, herdr tidak tersedia, dan model tidak tersedia tanpa fallback tersembunyi.
- Layout koordinator dominan tanpa merebut fokus atau merombak pane milik pengguna.
- Sesi worker selesai yang tetap terbuka tanpa pembersihan otomatis.

Daftar ini merupakan kriteria pengujian, bukan klaim bahwa pengujian telah dilakukan.
