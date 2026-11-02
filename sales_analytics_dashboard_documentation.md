# 📊 Sales Analytics Dashboard (Executive Overview)

Sebuah *Executive Dashboard* komprehensif yang dirancang untuk memantau performa penjualan, pencapaian target, profitabilitas, serta distribusi geografis dan kanal penjualan secara *real-time* untuk periode Januari–Desember 2025.

---

## 🚀 Fitur Utama (Key Features)

1. **High-Level Executive Metrics (KPI Cards):**
   - **Total Revenue:** Rp 14.13B (Akumulasi pendapatan bersih).
   - **Total Profit:** Rp 4.61B (Total keuntungan kotor/bersih yang dihasilkan).
   - **Profit Margin:** 32.6% (Rasio profitabilitas rata-rata secara keseluruhan).
   - **Unique Orders:** 2,706 total transaksi unik.
   - **Target Achievement:** 36.1% (Pencapaian aktual Rp 14.13B dari target total Rp 39.08B).

2. **Automated Insights & Actionable Recommendations:**
   - **Key Insights:** Menampilkan sorotan performa bulanan tertinggi (contoh: Maret 2025 dengan revenue Rp 1.39B), region terbaik (Denpasar), produk unggulan (Fashion Product 25), serta kanal dengan margin tertinggi (Marketplace, 32.7%).
   - **Actionable Advice:** Rekomendasi otomatis untuk memperkuat *campaign* di region dan kanal bernilai tinggi serta meninjau produk berdiskon tinggi.

3. **Filter Global Dinamis:**
   - Menyediakan filter interaktif berdasarkan: **Region**, **Category**, **Channel**, **Status** (e.g., Completed), dan **Month**.

4. **Visualisasi Data Lanjutan:**
   - **Revenue Trend vs Target:** Grafik garis perbandingan performa aktual pendapatan terhadap target bulanan (Jan–Dec 2025).
   - **Revenue Distribution Map:** Peta sebaran geografis Indonesia (Medan, Jakarta, Bandung, Surabaya, Makassar, Denpasar, dll.) untuk melihat titik konsentrasi penjualan.
   - **Regional Target Achievement:** Diagram batang persentase pencapaian target per kota/region.
   - **Top 10 Product Revenue Tree:** *Tree-map* visual yang menampilkan 10 produk teratas berdasarkan kontribusi pendapatan (Revenue).
   - **Channel Revenue & Margin:** Analisis komparatif performa pendapatan dan margin dari berbagai kanal penjualan.

---

## 🛠️ Teknologi yang Digunakan (Tech Stack)

- **Frontend / UI Framework:** Modern Dashboard UI (Tailwind CSS / Bootstrap / React / Vue - *sesuaikan dengan implementasi Anda*)
- **Data Visualization:** Chart.js / Recharts / D3.js / Mapbox (untuk peta distribusi regional)
- **Data Source:** SQL Database / REST API / CSV / Excel Data Warehouse

---

## 📂 Struktur Proyek (Project Structure)

```text
sales-analytics-dashboard/
│
├── public/                # Aset statis & gambar
├── src/
│   ├── components/        # Komponen UI modular (KPI Cards, Maps, Charts)
│   ├── assets/            # File CSS, Icon, dan Styling
│   ├── data/              # Contoh dataset atau hook API
│   ├── App.jsx            # Komponen utama aplikasi
│   └── main.js            # Titik masuk aplikasi (Entry point)
├── package.json           # Dependensi dan modul Node.js
└── README.md              # Dokumentasi proyek
```

---

## ⚙️ Cara Instalasi & Menjalankan (Getting Started)

Ikuti langkah-langkah berikut untuk menjalankan dashboard ini secara lokal di komputer Anda:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/username/sales-analytics-dashboard.git
   cd sales-analytics-dashboard
   ```

2. **Install Dependensi:**
   ```bash
   npm install
   ```

3. **Jalankan Mode Development:**
   ```bash
   npm run dev
   ```

4. **Buka di Browser:**
   Akses `http://localhost:5173` (atau port yang tertera di terminal Anda) melalui browser pilihan Anda.

---

## 📈 Panduan Penggunaan (Usage Guide)

- **Filter Data:** Gunakan *dropdown filter* di bagian atas (Region, Category, Channel, Status, Month) untuk menyaring data secara spesifik sesuai kebutuhan analisis Anda.
- **Analisis Insight:** Perhatikan kotak **Key Insights** dan **Action** di bawah metrik utama untuk mengambil keputusan bisnis yang cepat dan berbasis data (*data-driven decision*).

---

## 🤝 Kontribusi (Contributing)

Kontribusi, saran, dan laporan *bug* sangat diterima! Silakan buat *Pull Request* atau buka *Issue* baru pada repository ini.

---

## 📄 Lisensi (License)

Proyek ini dilisensikan di bawah [MIT License](LICENSE).