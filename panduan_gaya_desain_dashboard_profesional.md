# Panduan Gaya & Desain UI/UX Dashboard Analisis Data Profesional

Dokumen ini mendefinisikan standar estetika visual, palet warna, tipografi, dan tata letak (*layout*) untuk memastikan dashboard portofolio analitik memiliki standar eksekutif kelas dunia, terinspirasi langsung dari desain platform BI enterprise (Power BI & Excel Financial Dashboards).

---

## 1. Filosofi & Karakteristik Desain Eksekutif
* **Clean & Structured Grid:** Menggunakan tata letak berbasis kotak (*card-based container*) dengan sudut membulat (*rounded corners*) dan jarak antar-elemen yang konsisten (*white space* yang lapang).
* **Information Hierarchy:** Pimpinan atau *stakeholder* harus dapat memahami metrik utama (*KPIs*) dalam waktu di bawah 5 detik, diikuti oleh tren sekunder, dan detail tabel di bagian bawah.
* **Konsistensi Visual:** Kombinasi warna korporat yang tenang (seperti *Deep Navy*, *Slate Blue*, atau *Emerald Green*) dikombinasikan dengan indikator status fungsional (Hijau untuk performa positif, Merah/Oranye untuk penurunan atau risiko).

---

## 2. Skema Warna (*Color Palette*)
Palet warna dibagi berdasarkan peran fungsional agar tampilan dashboard terlihat bersih dan profesional:

* **Warna Utama (*Primary & Header*):**
  * *Deep Navy Blue* (`#0f223d` atau `#1b365d`): Digunakan untuk bar navigasi utama, header kartu, dan judul besar.
  * *Clean White/Light Gray* (`#f8f9fa` atau `#ffffff`): Latar belakang utama dashboard dan kartu kontainer.
* **Warna Aksen Grafik (*Chart Color Schemes*):**
  * *Classic Blue & Emerald:* Menggunakan gradasi biru profesional (`#1f77b4`) dan hijau finansial (`#2ca02c`) untuk menunjukkan pertumbuhan positif.
  * *Alert/Status Colors:* Hijau (`#2ecc71` / *Positive*), Merah (`#e74c3c` / *Negative*), dan Kuning/Oranye (`#f39c12` / *Warning/Pending*).
* **Warna Latar Kartu & Border:**
  * Kontainer kartu menggunakan latar putih bersih dengan bayangan tipis (*subtle box shadow*) dan garis tepi tipis (`#e2e8f0`) untuk menciptakan efek kedalaman (*depth*).

---

## 3. Komponen Utama Tampilan (*UI Components*)

### A. Sidebar Navigasi Kiri (*Sidebar Menu*)
* Berwarna gelap (*Dark Theme*) dengan logo atau judul aplikasi di bagian atas.
* Berisi menu navigasi halaman (*Overview*, *Products*, *Customers*, *Reports*, *Settings*) dilengkapi ikon emoji atau simbol yang intuitif.

### B. Header & Panel Filter Global (*Header & Global Filters*)
* Baris atas menampilkan judul halaman utama serta sub-judul deskriptif singkat.
* Dilengkapi *dropdown filters* (Filter berdasarkan Tahun, Kuartil, Wilayah, Kategori Produk) di sisi kanan atas, lengkap dengan tombol **Reset**.

### C. Kartu Metrik Utama / KPI Cards (Baris Pertama)
* Setiap kartu KPI berdiri sendiri dalam kotak putih berbingkai rapi.
* **Struktur Kartu KPI:**
  1. Label metrik di bagian atas (misal: *Total Sales*, *Total Orders*, *Profit Margin*).
  2. Nilai angka utama berukuran besar dan tebal (misal: `$739K` atau `Rp 45.860.00`).
  3. Indikator pertumbuhan di bagian bawah berupa persentase perubahan (misal: `▲ +9.4% vs last month`) disertai *sparkline* kecil atau ikon visual penunjang.

### D. Penataan Grafik (*Chart Layout & Structure*)
* **Distribusi 2 Kolom:** Grafik disusun secara simetris berdampingan (misal: Sisi kiri *Line Chart* tren waktu, sisi kanan *Bar Chart* kategori).
* **Format Tabel Ringkasan & Matriks:** Bagian bawah dashboard sering kali dialokasikan untuk tabel data terperinci atau matriks heatmap (seperti *Monthly Performance Summary* atau tabel status transaksi dengan label *Paid/Pending* berwarna).
* **Panel *Key Insights* (Wawasan Otomatis):** Menyediakan kolom khusus di sisi kanan atau bawah yang berisi poin-poin kesimpulan analisis otomatis (misal: *"Sales increased by 46.1% vs last month"*).

---

## 4. Standar Implementasi Teknis (Python / Streamlit / Plotly)
1. **Layout Lebar (*Wide Mode*):** Selalu aktifkan `layout="wide"` pada pengaturan halaman dashboard agar memanfaatkan layar secara maksimal layaknya aplikasi web profesional.
2. **Margin Grafik yang Rapi:** Pastikan setiap objek grafik Plotly memiliki *margin* minimal (`margin=dict(t=20, b=20, l=20, r=20)`) agar tidak terpotong dengan kontainer kartu.
3. **Tipografi Bersih:** Gunakan font standar sans-serif yang bersih (seperti Inter, Roboto, atau Segoe UI) dengan kontras warna teks yang tinggi agar mudah dibaca.