# 🚴‍♀️ Bike Sharing Dashboard  

Dashboard ini digunakan untuk menganalisis pola penggunaan sepeda berdasarkan berbagai faktor seperti cuaca, waktu, dan musim.  

---

## 🔧 Setup Environment
Sebelum menjalankan dashboard, Pastikan kamu telah menginstal **Python 3.7+** di perangkat. Untuk mengecek versi Python, jalankan perintah berikut:  
```bash
python --version
```
pastikan kamu sudah mengatur environment dengan benar. Kamu bisa memilih salah satu metode di bawah ini:  
#### **1️⃣Setup Environment dengan Anaconda**
Jika menggunakan **Anaconda**, jalankan perintah berikut:
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
#### **2️⃣ Setup Environment dengan Shell/Terminal (Tanpa Anaconda)**
Jika tidak menggunakan Anaconda, bisa menggunakan pipenv:
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
### **🚀 Menjalankan Streamlit App**
Setelah environment siap, jalankan Streamlit untuk melihat dashboard:
```bash
streamlit run dashboard.py
```
Tunggu beberapa detik, lalu dashboard akan terbuka otomatis di browser! 🎉

## **📌 Catatan**
Pastikan dataset (day_df.csv, hour_df.csv, main_data.csv) ada di direktori yang benar.
- Jika ada error ModuleNotFoundError, coba jalankan:
```bash
Copy
Edit
pip install -r requirements.txt
```
- Jika terjadi error terkait versi Streamlit, pastikan menggunakan versi terbaru atau downgrade jika diperlukan.

