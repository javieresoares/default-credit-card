import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model, scaler, dan label encoder
model = joblib.load("random_forest_best_model.pkl")
scaler = joblib.load("standard_scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("💳 Prediksi Default Kartu Kredit")
st.markdown("Masukkan data pengguna untuk memprediksi apakah pelanggan akan mengalami **default** pada pembayaran kartu kredit.")

# Ambil fitur yang dipakai saat training scaler
feature_names = scaler.feature_names_in_

# Placeholder nilai default yang realistis
default_values = {
    "LIMIT_BAL": 20000,
    "AGE": 35,
    "PAY_0": 0,
    "PAY_2": 0,
    "PAY_3": 0,
    "PAY_4": 0,
    "PAY_5": 0,
    "PAY_6": 0,
    "BILL_AMT1": 50000,
    "BILL_AMT2": 45000,
    "BILL_AMT3": 40000,
    "BILL_AMT4": 38000,
    "BILL_AMT5": 35000,
    "BILL_AMT6": 30000,
    "PAY_AMT1": 5000,
    "PAY_AMT2": 4500,
    "PAY_AMT3": 4000,
    "PAY_AMT4": 3500,
    "PAY_AMT5": 3000,
    "PAY_AMT6": 2500
}

# Nilai unik untuk fitur payment status (dari hasil eksplorasi sebelumnya)
pay_status_values = {
    "PAY_0": [2, -1, 0, -2, 1, 3, 4, 8, 7, 5, 6],
    "PAY_2": [2, 0, -1, -2, 3, 5, 7, 4, 1, 6, 8],
    "PAY_3": [-1, 0, 2, -2, 3, 4, 6, 7, 1, 5, 8],
    "PAY_4": [-1, 0, -2, 2, 3, 4, 5, 7, 6, 1, 8],
    "PAY_5": [-2, 0, -1, 2, 3, 5, 4, 7, 8, 6],
    "PAY_6": [-2, 2, 0, -1, 3, 6, 4, 7, 8, 5]
}

# Form input pengguna
user_input = {}
st.subheader("📥 Input Data Pengguna")

for feature in feature_names:
    if feature in pay_status_values:
        user_input[feature] = st.select_slider(
            f"{feature}",
            options=sorted(pay_status_values[feature]),
            value=default_values[feature]
        )
    else:
        user_input[feature] = st.number_input(
            f"{feature}",
            value=int(default_values.get(feature, 0)),
            step=1,
            format="%d"
        )

# Tombol prediksi
if st.button("Prediksi"):
    user_df = pd.DataFrame([user_input])

    # Pastikan semua kolom ada
    for col in feature_names:
        if col not in user_df.columns:
            user_df[col] = 0

    # Urutkan kolom sesuai urutan scaler
    user_df = user_df[feature_names]

    # Scaling
    user_scaled = scaler.transform(user_df)

    # Prediksi
    prediction = model.predict(user_scaled)
    predicted_label = label_encoder.inverse_transform(prediction)[0]

    st.success(f"🔍 Hasil Prediksi: **{predicted_label}**")
