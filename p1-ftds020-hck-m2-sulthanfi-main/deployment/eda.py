import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_eda():
    st.title("Analisis Eksplorasi Data (EDA)")

    # Cek apakah file sudah ada
    file_name = 'laptop_prices.csv'
    if os.path.exists(file_name):
        st.write(f"File '{file_name}' ditemukan. Membaca data dari file.")
        try:
            data = pd.read_csv(file_name)
            st.success("Data berhasil dimuat.")
        except Exception as e:
            st.error(f"Gagal memuat data: {e}")
            return  # Keluar jika ada kesalahan saat membaca file
    else:
        st.error(f"File '{file_name}' tidak ditemukan. Pastikan file ada di direktori yang sama dengan aplikasi.")
        return  # Keluar dari fungsi jika tidak ada data
    
    st.subheader("Beberapa Baris Pertama dari Dataset")
    st.writde(data.head())
    
    st.subheader("Deskripsi Statistik")
    st.write(data.describe())

    st.subheader("Visualisasi Distribusi")
    column = st.selectbox("Pilih kolom untuk visualisasi distribusi:", data.columns)
    
    if column:
        plt.figure(figsize=(10, 5))
        sns.histplot(data[column], bins=30, kde=True)
        st.pyplot(plt)

    st.subheader("Visualisasi Hubungan Antara Dua Kolom")
    x_col = st.selectbox("Pilih kolom untuk sumbu X:", data.columns)
    y_col = st.selectbox("Pilih kolom untuk sumbu Y:", data.columns)
    
    if x_col and y_col:
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=data, x=x_col, y=y_col)
        st.pyplot(plt)

    # Heatmap Korelasi
    st.subheader("Heatmap Korelasi")
    if st.checkbox("Tampilkan Heatmap Korelasi"):
        num_col = data.select_dtypes(include=['float64', 'int64']).columns  # Mengambil kolom numerik
        plt.figure(figsize=(15, 10))
        sns.heatmap(data[num_col].corr(), annot=True, fmt=".2f", cmap="coolwarm", xticklabels="auto")
        plt.title("Correlation Matrix")
        st.pyplot(plt)

    # Barplots untuk Price_euros vs. fitur lainnya
    st.subheader("Barplots: Price_euros vs. Fitur Lain")
    if st.checkbox("Tampilkan Barplots"):
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))
        sns.barplot(data=data, y='Price_euros', x='Ram', ax=axs[0][0])
        axs[0][0].set_title('Price_euros vs Ram')
        sns.barplot(data=data, y='Price_euros', x='ScreenW', ax=axs[0][1])
        axs[0][1].set_title('Price_euros vs ScreenW')
        sns.barplot(data=data, y='Price_euros', x='ScreenH', ax=axs[1][0])
        axs[1][0].set_title('Price_euros vs ScreenH')
        sns.barplot(data=data, y='Price_euros', x='CPU_freq', ax=axs[1][1])
        axs[1][1].set_title('Price_euros vs CPU_freq')
        
        plt.tight_layout()
        st.pyplot(fig)

if __name__ == '__main__':
    run_eda()
