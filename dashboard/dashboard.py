import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#gather data
temperature_df = pd.read_csv("dashboard/temperature.csv")
day_df = pd.read_csv("dashboard/dayy.csv")
grouped = pd.read_csv("dashboard/grouped.csv")

st.title('PROYEK ANALISIS DATA : BIKE SHARING')
st.header('Course Dicoding: Belajar Analisis Data dengan Python')


def suhu():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='temp', y='cnt', data=temperature_df, color='skyblue', label='Total rider')
    # sns.barplot(x='temp', y='registered', data=temperature_df, palette='Oranges', label='Registered Users')

    # Tambahkan judul dan label sumbu
    plt.title('Pengaruh Suhu Terhadap Penggunaan Sepeda')
    plt.xlabel('Rentang Suhu (°C)')
    plt.ylabel('Rata-rata Pengguna')
    plt.xticks(rotation=45)

    # Tampilkan legenda
    plt.legend()

    # Tampilkan chart
    st.pyplot(plt)

def tren():
    # Plot data
    plt.figure(figsize=(30, 8))
    plt.plot(day_df['casual'], label='Casual Users')
    plt.plot(day_df['registered'], label='Registered Users')

    # Judul dan label
    plt.title('Casual vs Registered Users (2011-1-1 to 2012-12-31)')
    plt.xlabel('Month')
    plt.ylabel('Number of Users')

    # Tampilkan legenda
    plt.legend()
    st.pyplot(plt)

def daily():
    # Buat pivot table dari DataFrame yang dikelompokkan
    pivot = grouped.pivot(index='weekday', columns='yr', values='cnt')

    # Buat plot dengan ukuran figure yang diinginkan
    ax = pivot.plot(kind='bar', stacked=False, figsize=(15, 6), width=0.9)

    # Atur judul dan label sumbu
    plt.title('Hari apa yang paling laris?')
    plt.xlabel('Hari')
    plt.ylabel('Banyaknya Pengguna')
    plt.xticks(rotation=15)

    # Tambahkan nilai di atas masing-masing bar
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

    # Tampilkan plot
    st.pyplot(plt)


# no.1 : chart suhu terhadap penggunaan sepeda
st.subheader('1. Pengaruh Suhu terhadap Penggunaan Sepeda')
suhu()
st.write("""
Data diagram ini diperoleh dari perhitungan pengguna sepeda baik casual maupun registered
dalam setiap jam selama 2 tahun. Diagram ini menunjukkan bahwa frekuensi pengguna sepeda
meningkat seiring dengan meningkatnya suhu rata-rata lingkungan.
""")

# no.2 : line chart perkembangan casual dan registered user
st.subheader('2. Perkembangan Casual dan Registered User')
tren()
st.write("""
Diagram line diatas diambil dari perhitungan pengguna casual dan registered selama 2 tahun.
Diagram ini menunjukkan adanya peningkatan pengguna jasa bike sharing dari tahun ke tahun.
""")

# no.3 : clustered bar chart penggunaan sepeda setiap harinya dalam 2 tahun
st.subheader('3. Penggunaan Sepeda Setiap Harinya dalam 2 Tahun')
daily()
st.write("""
Diagram ini diambil dari akumulasi total pengguna jasa bike sharing setiap harinya.
Perbedaan jumlah pengguna di tiap hari dipengaruhi oleh beberapa faktor lingkungan 
seperti suhu, kelembapan, cuaca, dsb.
""")

st.subheader('Kesimpulan Analisis:')
st.write("""
1. Pengguna lebih menyukai penggunaan sepeda ketika suhu sedang hangat
2. Terdapat peningkatan pengguna (registered) yang signifikan dari tahun 2011 ke tahun 2012, hal ini menunjukkan sistem bike sharing ini cukup efektif
3. Untuk tahun 2011 pengguna paling banyak adalah ketika hari selasa sedangkan pada tahun 2012 adalah hari kamis, hal ini sangat didominasi oleh beberapa faktor seperti hari libur dan cuaca setiap tahun

Adapun beberapa poin menarik yang bisa dilihat dari hasil analisis ini:
Berdasarkan data, cuaca dan hari libur atau akhir pekan berpengaruh pada jumlah penumpang sistem berbagi sepeda. 
Suhu tinggi meningkatkan jumlah penumpang, sedangkan kelembaban tinggi menurunkannya. 
Di hari kerja, perjalanan santai lebih sedikit karena banyak pengguna yang berangkat kerja, menciptakan dua puncak kepadatan pengguna. 
Di hari libur, pola penumpang berbeda yakni hanya satu puncak kepadatan pengguna.
""")

st.caption('Copyright (c) 2023')