
# 🏦 Default Credit Card Prediction

Aplikasi **Machine Learning** berbasis **Streamlit** untuk memprediksi kemungkinan seorang nasabah kartu kredit akan mengalami **default** (gagal bayar) pada bulan berikutnya.

## 🚀 Live Demo

👉 **Check out the deployed Streamlit app here:**  
[https://default-credit-card-prediction.streamlit.app/](https://default-credit-card-prediction.streamlit.app/)

## 📁 Struktur Proyek

```
default-credit-card/
├── CreditCard.ipynb                  # Notebook eksplorasi & training model
├── CreditCard.ipynb - Colab.pdf      # Versi PDF notebook
├── app.py                            # Aplikasi web Streamlit
├── credit_card_default_clean.csv     # Dataset hasil pembersihan
├── default of credit card clients.xls# Dataset asli
├── label_encoder.pkl                 # Label encoder target
├── random_forest_best_model.pkl      # Model Random Forest terbaik
├── requirements.txt                  # Daftar dependensi
├── standard_scaler.pkl               # Scaler fitur numerik
```

## 🚀 Fitur Aplikasi

- Input data nasabah secara manual (via UI)
- Validasi nilai input dengan batasan yang sesuai
- Normalisasi fitur menggunakan `StandardScaler`
- Prediksi menggunakan model `Random Forest`
- Interpretasi hasil prediksi: apakah nasabah berisiko gagal bayar

## 📊 Dataset

- Sumber: [UCI Machine Learning Repository - Default of Credit Card Clients Dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)
- Fitur penting yang digunakan mencakup:
  - Batas kredit (`LIMIT_BAL`)
  - Usia (`AGE`)
  - Riwayat keterlambatan pembayaran (`PAY_0` hingga `PAY_6`)
  - Jumlah tagihan bulan sebelumnya (`BILL_AMT1` hingga `BILL_AMT6`)
  - Jumlah pembayaran sebelumnya (`PAY_AMT1` hingga `PAY_AMT6`)

## 🧪 Cara Menjalankan Aplikasi

1. **Clone repositori ini**
   ```bash
   git clone https://github.com/javieresoares/default-credit-card.git
   cd default-credit-card
   ```

2. **Buat virtual environment dan aktifkan**
   ```bash
   python -m venv venv
   source venv/bin/activate     # MacOS/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependensi**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit**
   ```bash
   streamlit run app.py
   ```

## 🛠 Model & Preprocessing

- Model: `RandomForestClassifier` (dengan hyperparameter tuning)
- Fitur diskalakan menggunakan `StandardScaler`
- Target label di-encode menggunakan `LabelEncoder`

## 📦 Dependencies

Tercantum dalam `requirements.txt`, contoh utama:
- `streamlit`
- `pandas`
- `scikit-learn`
- `numpy`
- `joblib`

## 📌 Catatan

- Pastikan file `random_forest_best_model.pkl`, `standard_scaler.pkl`, dan `label_encoder.pkl` tersedia di direktori proyek.
- Aplikasi ini dimaksudkan untuk edukasi dan demonstrasi, bukan untuk keputusan keuangan nyata.

## 👨‍💻 Author

**Javier Soares**  
GitHub: [@javieresoares](https://github.com/javieresoares)
