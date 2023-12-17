
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV atau sumber data lainnya
all_df = pd.read_csv('all_data.csv')

# Menampilkan judul dashboard
st.title('Dashboard Analisis Data Peminjaman Sepeda')

# Visualisasi 1: Tren Peminjaman Sepeda sepanjang Waktu
fig1, ax1 = plt.subplots()
ax1.plot(all_df['dteday'], all_df['cnt'], label='Jumlah Total Peminjaman', color='blue')
ax1.set_title('Tren Peminjaman Sepeda Sepanjang Waktu')
ax1.set_xlabel('Tanggal')
ax1.set_ylabel('Jumlah Total Peminjaman')
ax1.legend()
st.pyplot(fig1)

st.markdown("tren peminjaman sepeda mengalami perubahan pada tiap bulan dalam sepanjang tahun. tren yang terjadi pada rentang 2011 dan 2012 mengalami peningkatan. bulan pertengahan adalah puncak jumlah tertinggi peminjaman sepeda pada tiap tahunnya.")

# Visualisasi 2: Pengaruh Cuaca terhadap Peminjaman Sepeda
cuaca_agregat = all_df.groupby('weathersit')['cnt'].sum().reset_index()
cuaca_agregat['weathersit'] = cuaca_agregat['weathersit'].replace({
    1: 'Cerah',
    2: 'Berawan/Mist',
    3: 'Hujan Ringan/Salju',
    4: 'Hujan Lebat/Salju'
})
fig2, ax2 = plt.subplots()
ax2.bar(cuaca_agregat['weathersit'], cuaca_agregat['cnt'], color='skyblue')
ax2.set_title('Pengaruh Cuaca terhadap Peminjaman Sepeda')
ax2.set_xlabel('Jenis Cuaca')
ax2.set_ylabel('Jumlah Total Peminjaman')
st.pyplot(fig2)

st.markdown("Cuaca memiliki pengaruh dalam jumlah peminjaman sepeda. cuaca cerah meningkatkan jumlah peminjaman sepeda, sedangkan pada cuaca berawan dan hujan/salju jumlah peminjaman sepeda menurun")

# Visualisasi 3: Pengaruh Hari Kerja terhadap Peminjaman Sepeda
hari_kerja_agregat = all_df.groupby('weekday')['cnt'].sum().reset_index()
hari_kerja_agregat['weekday'] = hari_kerja_agregat['weekday'].replace({
    0: 'Senin',
    1: 'Selasa',
    2: 'Rabu',
    3: 'Kamis',
    4: 'Jumat',
    5: 'Sabtu',
    6: 'Minggu'
})
fig3, ax3 = plt.subplots()
ax3.bar(hari_kerja_agregat['weekday'], hari_kerja_agregat['cnt'], color='green')
ax3.set_title('Pengaruh Hari Kerja terhadap Peminjaman Sepeda')
ax3.set_xlabel('Hari dalam Seminggu')
ax3.set_ylabel('Jumlah Total Peminjaman')
st.pyplot(fig3)

st.markdown("Hari kerja dan akhir pekan tidak mempengaruhi pola peminjaman sepeda dan relatif stabil")

# Visualisasi 4: Pengaruh Suhu terhadap Peminjaman Sepeda
fig4, ax4 = plt.subplots()
ax4.scatter(all_df['temp'], all_df['cnt'], color='orange')
ax4.set_title('Pengaruh Suhu terhadap Peminjaman Sepeda')
ax4.set_xlabel('Suhu (Celsius)')
ax4.set_ylabel('Jumlah Total Peminjaman')
st.pyplot(fig4)

st.markdown("Pada plot scatter, suhu mempengaruhi tingkat peminjaman sepeda. konsumen cenderung melakukan peminjaman sepeda pada suhu hangat menuju panas")
