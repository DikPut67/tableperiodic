# ⚗️ Tabel Periodik Unsur Kimia — Golongan 1A hingga 8A

Aplikasi web interaktif tabel periodik unsur kimia yang mencakup **Golongan 1A sampai 8A** (Golongan Utama), dibangun dengan **Python + Streamlit**.

## ✨ Fitur

- 🗂️ **Tampilan Tabel Periodik Visual** — Warna-warni per golongan, hover effect
- 🔍 **Detail Unsur Interaktif** — Pilih golongan & unsur, lihat semua properti
- 📊 **Tabel Data Lengkap** — Filter per golongan, urutkan, unduh CSV
- 🎨 **Legenda Golongan** — Warna berbeda tiap golongan

## 📋 Informasi Yang Ditampilkan

| Properti | Keterangan |
|---|---|
| Nomor Atom | Jumlah proton dalam inti |
| Lambang | Simbol kimia unsur |
| Nama Unsur | Nama dalam bahasa Indonesia |
| Massa Atom | Dalam satuan u (amu) |
| Titik Didih | Dalam derajat Celsius (°C) |
| Titik Leleh | Dalam derajat Celsius (°C) |
| Massa Jenis | Dalam g/cm³ |
| Tingkat Oksidasi | Semua tingkat oksidasi umum |
| Struktur Elektron | Konfigurasi elektron |

## 🚀 Cara Menjalankan Secara Lokal

```bash
# 1. Clone atau unduh repository ini
git clone https://github.com/USERNAME/REPO-NAME.git
cd REPO-NAME

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi
streamlit run app.py
```

Aplikasi akan terbuka di browser: `http://localhost:8501`

## ☁️ Deploy ke Streamlit Cloud (Gratis)

1. **Upload ke GitHub:**
   - Buat repository baru di [github.com](https://github.com)
   - Upload file `app.py` dan `requirements.txt`

2. **Deploy di Streamlit Cloud:**
   - Buka [share.streamlit.io](https://share.streamlit.io)
   - Login dengan akun GitHub
   - Klik **"New app"**
   - Pilih repository, branch `main`, dan file `app.py`
   - Klik **"Deploy!"**
   - Tunggu beberapa menit — aplikasi akan online secara gratis!

## 📦 Struktur File

```
📁 repository/
├── app.py            ← Kode utama Streamlit
├── requirements.txt  ← Daftar library Python
└── README.md         ← Dokumentasi ini
```

## 🧪 Unsur yang Tercakup

| Golongan | Nama | Unsur |
|---|---|---|
| 1A | Logam Alkali | H, Li, Na, K, Rb, Cs, Fr |
| 2A | Logam Alkali Tanah | Be, Mg, Ca, Sr, Ba, Ra |
| 3A | Golongan Boron | B, Al, Ga, In, Tl, Nh |
| 4A | Golongan Karbon | C, Si, Ge, Sn, Pb, Fl |
| 5A | Golongan Nitrogen | N, P, As, Sb, Bi, Mc |
| 6A | Kalkogen | O, S, Se, Te, Po, Lv |
| 7A | Halogen | F, Cl, Br, I, At, Ts |
| 8A | Gas Mulia | He, Ne, Ar, Kr, Xe, Rn, Og |

**Total: 55 unsur** (termasuk unsur sintetis periode 7)

---
Data berdasarkan **IUPAC** (International Union of Pure and Applied Chemistry)
