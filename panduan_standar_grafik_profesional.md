# Panduan Komprehensif Pemilihan Grafik & Visualisasi Data Profesional

Dokumen ini mendefinisikan standar profesional dalam pemilihan jenis grafik (*chart*) untuk proyek *Dashboard Analisis Data*. Pemilihan visualisasi didasarkan pada karakteristik data, tujuan analisis, dan kebutuhan bisnis agar informasi dapat dipahami oleh *stakeholder* (pengambil keputusan) dalam waktu kurang dari 5 detik.

---

## 1. Prinsip Utama Visualisasi Data
* **Kejelasan (*Clarity*):** Grafik harus langsung menyampaikan pesan tanpa membuat penonton bingung.
* **Relevansi (*Relevance*):** Jenis grafik harus disesuaikan secara presisi dengan tipe data dan tujuan statistik.
* **Variasi (*Variety*):** Menghindari penggunaan satu jenis grafik saja untuk menjaga keterlibatan visual dan ketepatan penyampaian informasi.

---

## 2. Kategori & Panduan Pemilihan Jenis Grafik

### A. Analisis Tren Waktu (*Time-Series*)
Digunakan untuk melacak perubahan metrik seiring berjalannya waktu.
* **Line Chart (Grafik Garis):** Menunjukkan tren berkelanjutan dari satu atau beberapa variabel waktu (contoh: Tren pendapatan bulanan).
* **Area Chart / Stacked Area:** Menekankan volume atau kontribusi kumulatif dari waktu ke waktu (contoh: Pertumbuhan basis pengguna berdasarkan perangkat).
* **Sparklines:** Mikro-tren untuk ditaruh di dalam kartu KPI agar hemat tempat.

### B. Perbandingan Kategori (*Comparison*)
Digunakan untuk membandingkan nilai antar kelompok, item, atau kategori.
* **Bar Chart / Horizontal Bar Chart:** Pilihan terbaik untuk membandingkan kategori. Versi horizontal wajib digunakan jika nama kategori/label teksnya panjang (contoh: Top 10 produk terlaris).
* **Grouped / Clustered Bar Chart:** Membandingkan dua atau lebih variabel berseri dalam satu kategori berdampingan.
* **Bullet Chart:** Membandingkan capaian aktual terhadap target dengan indikator kualitatif.

### C. Komposisi & Proporsi (*Composition & Part-to-Whole*)
Digunakan untuk melihat bagaimana total nilai terbagi menjadi bagian-bagian komponennya.
* **Treemap:** Menampilkan data hierarki menggunakan blok-blok persegi panjang, sangat unggul untuk data dengan jumlah kategori yang banyak (*high cardinality*).
* **Donut Chart / Pie Chart:** Hanya digunakan untuk proporsi sederhana (maksimal 3–5 kategori) dengan total 100%.
* **Waterfall Chart:** Menunjukkan bagaimana nilai awal dipengaruhi oleh penambahan dan pengurangan beruntun (contoh: Rekonsiliasi laba bersih).

### D. Distribusi Statistik & Frekuensi (*Distribution*)
Digunakan untuk memahami sebaran nilai di dalam satu variabel tunggal (mendeteksi pola normal, skewness, atau anomali).
* **Histogram:** Membagi data kontinu ke dalam *bin* untuk melihat frekuensi kemunculan.
* **Box Plot (Box-and-Whisker Plot):** Menampilkan ringkasan statistik 5 poin serta mendeteksi data ekstrem (*outliers*).
* **Density Plot / Violin Plot:** Versi halus dari histogram atau kombinasi *box plot* untuk melihat kepadatan probabilitas.

### E. Hubungan & Korelasi (*Relationship & Correlation*)
Digunakan untuk melihat apakah ada hubungan sebab-akibat atau korelasi antarvariabel.
* **Scatter Plot:** Memetakan titik data pada sumbu X dan Y untuk melihat pola korelasi (contoh: Diskon vs Volume Penjualan).
* **Bubble Chart:** Variabel ketiga direpresentasikan melalui ukuran lingkaran.
* **Heatmap (Peta Panas):** Menampilkan kekuatan korelasi statistik antarvariabel menggunakan gradasi warna matriks.

### F. Geospasial & Alur (*Geospatial & Flow*)
Digunakan jika data memiliki atribut lokasi geografis atau proses tahapan bisnis.
* **Choropleth Map:** Menampilkan data metrik berdasarkan wilayah geografis (provinsi/kota).
* **Funnel Chart (Grafik Corong):** Melacak penurunan tahapan proses konversi (*conversion rate*) dari awal hingga akhir.

---

## 3. Aturan Desain Profesional untuk *Stakeholder*
1. **Gunakan Kartu KPI (*Metric Cards*):** Selalu letakkan ringkasan angka penting di bagian atas dashboard beserta indikator pertumbuhan.
2. **Batasi Jumlah Kategori:** Batasi maksimal 5–7 kategori utama pada grafik proporsi/batang agar tidak sesak secara visual.
3. **Palet Warna Konsisten:** Gunakan warna yang selaras dan profesional, hindari warna yang terlalu mencolok secara berlebihan.
4. **Bahasa yang Intuitif:** Semua label sumbu, judul grafik, dan keterangan metrik wajib menggunakan bahasa Indonesia yang baku, profesional, dan mudah dipahami manajemen.