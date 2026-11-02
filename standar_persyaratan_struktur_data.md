# Panduan Standar Persyaratan & Struktur Data (*Dashboard Data Requirements*)

Dokumen ini mendefinisikan standar teknis mengenai skema data mentah (*schema*), tipe data, penanganan nilai kosong (*missing values*), serta format sampel data yang wajib dipenuhi sebelum data divisualisasikan ke dalam dashboard analisis.

---

## 1. Spesifikasi Skema Data Utama (*Dataset Schema*)
Setiap sumber data (file CSV, Excel, atau database) yang digunakan dalam proyek portofolio harus memiliki kolom-kolom inti dengan spesifikasi tipe data berikut:

| Nama Kolom | Tipe Data (*Data Type*) | Deskripsi / Definisi Bisnis |
| :--- | :--- | :--- |
| `Tanggal` | `Datetime` (YYYY-MM-DD) | Tanggal terjadinya transaksi atau aktivitas bisnis. |
| `Kategori` | `String` / *Categorical* | Kategori produk atau unit bisnis utama (contoh: Elektronik, Pakaian). |
| `Wilayah` | `String` / *Categorical* | Lokasi geografis atau cabang operasional (contoh: Jakarta, Surabaya). |
| `Pendapatan` | `Float` / *Currency* | Nilai moneter per unit transaksi (harga satuan). |
| `Jumlah_Terjual` | `Integer` | Kuantitas produk yang terjual dalam satu transaksi. |
| `Kepuasan_Pelanggan` | `Integer` / *Score* | Skor penilaian kepuasan pelanggan (skala 1 hingga 5). |

---

## 2. Aturan Pra-Pemrosesan Data (*Data Preprocessing & Cleaning*)
Sebelum data diolah oleh modul visualisasi, AI atau *Data Analyst* wajib menjalankan langkah-langkah pembersihan berikut:
1. **Standarisasi Nama Kolom:** Menghapus spasi berlebih, menggunakan format *snake_case* (`nama_kolom`), dan menghindari karakter khusus atau huruf kapital acak.
2. **Konversi Tipe Data Waktu:** Memastikan kolom tanggal telah dikonversi ke format `datetime` Pandas agar fungsi pengelompokan waktu (*time-series aggregation*) berjalan akurat.
3. **Penanganan Nilai Kosong (*Missing Values*):** 
   * Baris dengan nilai kosong pada kolom penting (`Tanggal`, `Pendapatan`) harus diimputasi atau dihapus jika jumlahnya minoritas.
   * Nilai numerik kosong dapat diisi dengan nilai median atau rata-rata berdasarkan kelompoknya.
4. **Perhitungan Kolom Turunan (*Derived Columns*):** Menambahkan kolom kalkulasi bisnis penting secara otomatis, seperti `Total_Penjualan` ($\text{Pendapatan} \times \text{Jumlah\_Terjual}$) untuk memudahkan agregasi metrik KPI.

---

## 3. Format Sampel Data (Contoh Struktur JSON / CSV)
```csv
Tanggal,Kategori,Wilayah,Pendapatan,Jumlah_Terjual,Kepuasan_Pelanggan
2025-01-01,Elektronik,Jakarta,4500000,2,5
2025-01-02,Pakaian,Surabaya,750000,4,4
2025-01-03,Kecantikan,Bandung,1200000,3,5
```

---

## 4. Integrasi dengan Sistem Dashboard
* **Caching Data:** Gunakan dekorator pemrosesan data (seperti `@st.cache_data` pada Streamlit) untuk mengoptimalkan performa pemuatan data agar dashboard dapat merespons perubahan filter secara instan tanpa melakukan *re-loading* file berulang kali.