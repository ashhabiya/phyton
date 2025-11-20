import streamlit as st
from datetime import date

# 1. Fungsi inti untuk menghitung usia
def hitung_usia(tahun_lahir, tahun_sekarang=None):
    """Menghitung usia (hanya tahun) berdasarkan tahun lahir."""
    
    # Ambil tahun sekarang dari sistem jika tidak disetel
    if tahun_sekarang is None:
        tahun_sekarang = date.today().year
        
    usia = tahun_sekarang - tahun_lahir
    return usia, tahun_sekarang

# 2. Judul dan Deskripsi Aplikasi Streamlit
st.title("🧮 Kalkulator Usia Sederhana")
st.markdown("Aplikasi ini menghitung usia Anda berdasarkan tahun lahir.")

# 3. Input Pengguna menggunakan komponen Streamlit
# Tahun sekarang disetel dinamis atau bisa disetel manual
tahun_maks = date.today().year
thn_lahir = st.number_input(
    "Masukkan **Tahun Lahir** Anda:",
    min_value=1900,
    max_value=tahun_maks,
    value=2000, # Nilai default
    step=1,
    format="%d"
)

# 4. Tombol untuk menjalankan perhitungan
if st.button("Hitung Usia"):
    # Pastikan input tahun lahir valid (tidak di masa depan)
    if thn_lahir > tahun_maks:
        st.error("Tahun lahir tidak boleh di masa depan!")
    else:
        # Panggil fungsi hitung
        usia_saat_ini, thn_sekarang = hitung_usia(thn_lahir)

        # 5. Output Hasil
        st.success(f"🎉 **Hasil Perhitungan:**")
        st.info(f"Jika Anda lahir tahun **{thn_lahir}** dan sekarang adalah tahun **{thn_sekarang}**, usia Anda adalah:")
        
        # Tampilkan usia dengan format besar
        st.metric(label="Usia Anda", value=f"{usia_saat_ini} tahun")

# Catatan kecil
st.caption("Perhitungan ini didasarkan pada selisih tahun saja.")