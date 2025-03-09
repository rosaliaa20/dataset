import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
import calendar
import os

from PIL import Image

# Load dataset
day_df = pd.read_csv('https://raw.githubusercontent.com/rosaliaa20/dataset/refs/heads/main/data/day_df.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/rosaliaa20/dataset/refs/heads/main/data/hour_df.csv')
all_df = pd.read_csv('https://raw.githubusercontent.com/rosaliaa20/dataset/refs/heads/main/dashboard/main_data.csv')

# Convert 'dateday' to datetime
all_df['dateday'] = pd.to_datetime(all_df['dateday'])
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Sidebar
with st.sidebar:

    # Atur lebar gambar
    st.sidebar.image('https://raw.githubusercontent.com/rosaliaa20/dataset/main/dashboard/user.jpeg', caption="Profile Picture")

    st.markdown("""
        **👤 Nama:** Rosalia Indah Dwi Putriningsih  
        **📧 Email:** [senjanindya05@gmail.com](mailto:senjanindya05@gmail.com)  
        **🆔 Username:** rosaliaindah
    """)

    # Rentang waktu
    min_date, max_date = all_df['dateday'].min(), all_df['dateday'].max()
    start_date, end_date = st.date_input("Pilih Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])

# Filter dataset sesuai pilihan user
filtered_df = all_df[(all_df['dateday'] >= pd.to_datetime(start_date)) & (all_df['dateday'] <= pd.to_datetime(end_date))]

# Filter juga untuk day_df agar selaras dengan rentang waktu
filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Main title
st.title("📊 Bike Sharing Dashboard")

# 1. Perbedaan Penggunaan Kasual vs Terdaftar
st.subheader("👥 Pola Penggunaan: Kasual vs Terdaftar")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_day_df, x='dteday', y='casual', label='Casual', marker='o')
sns.lineplot(data=filtered_day_df, x='dteday', y='registered', label='Registered', marker='o')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Pengguna")
st.pyplot(fig)

# 2. Korelasi Faktor terhadap Penyewaan
st.subheader("📊 Korelasi Faktor dengan Jumlah Penyewaan")
numeric_cols = filtered_day_df.select_dtypes(include=[np.number])
correlation_matrix = numeric_cols.corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# 3. Visualisasi Tren Penyewaan Sepeda per Bulan**
st.subheader("📊 Tren Penggunaan Sepeda Sepanjang Tahun (Per Bulan)")
filtered_day_df["month"] = filtered_day_df["dteday"].dt.month
rental_per_month = filtered_day_df.groupby("month")["cnt"].sum()

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(rental_per_month.index, rental_per_month.values, color="skyblue", edgecolor="black")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Tren Penyewaan Sepeda per Bulan")
ax.set_xticks(range(1, 13))
ax.set_xticklabels([calendar.month_abbr[i] for i in range(1, 13)])  # Nama bulan (Jan, Feb, ...)
st.pyplot(fig)

st.write("\n\n💡 **Insight:** Faktor yang paling berpengaruh terhadap jumlah penyewaan sepeda adalah suhu, kelembaban, dan musim.")
