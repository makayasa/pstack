# pstack orchestration

Istilah untuk pembagian kerja agent yang dapat dipantau dan diintervensi pengguna.

## Language

**Koordinator**:
Agent yang membagi tugas kepada worker, menilai hasilnya, dan menentukan langkah berikutnya.
_Avoid_: Orchestrator, supervisor

**Worker**:
Agent yang menerima tugas dari koordinator dan melaporkan hasil pekerjaan tersebut.
_Avoid_: Subagent, delegate

**Pemantauan manual**:
Kemampuan pengguna untuk melihat pekerjaan agent yang berjalan dan mengintervensinya tanpa wajib menyetujui setiap langkah.
_Avoid_: Persetujuan per langkah

**Pengambilalihan manual**:
Peralihan kendali atas worker dari koordinator kepada pengguna sampai pengguna mengembalikan kendali tersebut.
_Avoid_: Pemantauan manual, penghentian worker

**Budget reasoning**:
Pilihan tingkat reasoning untuk pemetaan model per peran dalam pstack, bukan batas biaya uang atau jumlah worker.
_Avoid_: Batas biaya, batas paralelisme
