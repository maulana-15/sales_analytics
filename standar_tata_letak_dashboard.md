# Panduan Standar Tata Letak & Struktur Grid Dashboard (*Dashboard Layout & Grid Standards*)

Dokumen ini mendefinisikan prinsip-prinsip desain struktural dan hierarki visual untuk memastikan tata letak dashboard analitik tertata rapi, mudah dipahami dalam 5 detik pertama oleh *stakeholder*, serta responsif di berbagai ukuran layar.

---

## 1. Prinsip Utama Hierarki Visual (*Visual Hierarchy*)
* **Aturan Membaca (Z-Pattern & F-Pattern):** Mata penonton secara alami bergerak dari kiri atas ke kanan atas, lalu turun ke bawah. Oleh karena itu, informasi paling krusial harus diletakkan di zona paling atas.
* **Prinsip *Top-Down Summary*:** Informasi umum dengan level tinggi (*executive summary*) diletakkan di bagian atas, diikuti dengan analisis mendetail dan grafik eksploratif di bagian bawah.

---

## 2. Pembagian Zona Layout Halaman Dashboard

Sebuah halaman dashboard profesional harus dibagi secara konsisten menjadi 3 zona utama:

### A. Header & Kontrol Global (*Top Section*)
* **Judul Dashboard & Status:** Terletak di pojok kiri atas (misal: *Sales Analytics Dashboard* atau *Trading Performance*).
* **Global Filters / Slicer Bar:** Terletak di sebelah kanan judul atau di dalam *Sidebar* khusus. Berisi filter waktu (*Date Range*), kategori produk, wilayah, atau tombol *Reset*.

### B. Baris Kartu KPI / Metrik Utama (*KPI Summary Cards*)
* **Posisi:** Tepat di bawah Header utama (Baris ke-2).
* **Struktur:** Berisi 4 hingga 6 kartu metrik penting (misal: *Total Pendapatan*, *Total Pesanan*, *Margin Keuntungan*, *Rata-rata Nilai Pesanan*).
* **Komponen di Dalam Kartu:** 
  * Judul metrik (ukuran kecil, warna sekunder).
  * Angka utama (ukuran besar, *bold*).
  * Indikator pertumbuhan / tren persentase (misal: hijau untuk naik, merah untuk turun) beserta *mini sparkline* di bawahnya.

### C. Grid Area Grafik Utama & Detail (*Main Content Grid*)
* **Baris Tengah (Primary Charts):** Grafik dengan prioritas tertinggi untuk melihat tren waktu (*Line/Area Chart*) dan perbandingan utama (*Bar Chart / Treemap*).
* **Baris Bawah (Secondary / Deep-Dive Data):** Tabel data transaksi terkini (*Recent Data Table*), analisis korelasi (*Heatmap*), atau ringkasan wawasan otomatis (*Key Insights*).

---

## 3. Standar *Spacing* dan Penataan Ruang (*White Space*)
* **Padding & Margin:** Selalu berikan ruang kosong (*white space*) yang cukup di sekeliling kartu dan grafik agar tampilan tidak terasa padat (*cluttered*).
* **Konsistensi Kartu:** Setiap komponen grafik atau metrik harus dibungkus dalam *container* (kartu putih dengan sudut melengkung halus dan bayangan tipis/*subtle border*) agar memiliki batas visual yang jelas terhadap latar belakang halaman.