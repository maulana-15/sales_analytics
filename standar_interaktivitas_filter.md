# Panduan Standar Interaktivitas & Kontrol Pengguna (*Dashboard Interactivity & Filters*)

Dokumen ini mendefinisikan aturan dan standar teknis mengenai bagaimana pengguna (*stakeholder*) berinteraksi dengan dashboard, mekanisme filter global, serta responsivitas kontrol data untuk memastikan pengalaman pengguna yang intuitif dan cepat.

## 1. Prinsip Utama Interaktivitas Dashboard
* **Respon Instan (*Real-time Responsiveness*):** Setiap perubahan pada kontrol filter harus langsung memperbarui seluruh kartu KPI dan grafik dalam waktu kurang dari 1 detik.
* **Kejelasan Lingkup Filter (*Filter Scope Clarity*):** Pengguna harus selalu tahu filter mana yang sedang aktif dan bagaimana filter tersebut memengaruhi keseluruhan tampilan data.
* **Kemudahan Reset (*Easy Reset*):** Selalu sediakan opsi atau tombol untuk mengembalikan semua filter ke kondisi awal (*default all*).

## 2. Komponen Kontrol & Slicer (*User Controls*)

### A. Filter Global di Sidebar (*Global Sidebar Filters*)
* **Filter Tanggal / Rentang Waktu (*Date Range Picker*):** Kontrol utama untuk memfilter data berdasarkan periode waktu tertentu (misal: Harian, Bulanan, atau Rentang Tanggal Kustom).
* **Filter Kategori & Wilayah (*Multi-select Dropdowns*):** Memungkinkan pengguna memilih satu atau beberapa kategori produk dan wilayah operasional secara bersamaan.
* **Tombol Aksi (*Action Buttons*):** Tombol interaktif untuk mereset filter (*Reset Filters*) atau mengekspor ringkasan data.

### B. Interaksi Antar-Grafik (*Cross-Filtering*)
* **Filter Silang Berbasis Plotly:** Memungkinkan pengguna mengklik elemen tertentu pada grafik (misal: mengklik batang kategori "Elektronik" pada *Bar Chart*) untuk memfilter data secara otomatis pada grafik lainnya di halaman yang sama.
* **Tooltips Informatif:** Setiap grafik wajib menampilkan *hover tooltip* yang akurat, menampilkan nilai presisi, persentase kontribusi, dan label kategori saat kursor diarahkan ke titik data.

## 3. Penanganan Kondisi Data Kosong Akibat Filter (*Empty State Handling*)
* **Peringatan Kondisi Kosong:** Jika kombinasi filter yang dipilih oleh pengguna tidak menghasilkan data, dashboard **tidak boleh *crash* atau *error***.
* **Pesan UI yang Informatif:** Tampilkan pesan yang ramah kepada pengguna (contoh: *"⚠️ Tidak ada data yang ditemukan untuk filter yang dipilih. Silakan sesuaikan kembali kriteria filter."*).

## 4. Standar Implementasi Teknis (Streamlit/Python)
* Gunakan fungsi reaktif Streamlit (`st.selectbox`, `st.multiselect`, `st.date_input`) dengan penamaan variabel yang jelas.
* Terapkan pemfilteran DataFrame secara berantai (*chained filtering*) agar logika pembersihan data tetap bersih dan mudah dibaca oleh agen AI atau pengembang.