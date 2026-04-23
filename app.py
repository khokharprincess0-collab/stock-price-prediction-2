import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Stock Prediction App", layout="centered")

st.title("📈 Stock Prediction App (Clean & Fixed)")
st.write("Upload your CSV file and predict stock values")

# ---------------------------
# 1. Upload CSV
# ---------------------------
file = st.file_uploader("Upload CSV File", type=["csv"])

if file:

    df = pd.read_csv(file)
    st.subheader("📊 Raw Data")
    st.write(df.head())

    # ---------------------------
    # 2. CLEAN DATA
    # ---------------------------

    st.subheader("🧹 Data Preprocessing")

    # Fill missing values
    df = df.dropna()

    # Convert categorical columns automatically
    label_encoders = {}

    for col in df.columns:
        if df[col].dtype == "object":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

    st.write("✅ Data after encoding:")
    st.write(df.head())

    # ---------------------------
    # 3. Select Target
    # ---------------------------
    target_column = st.selectbox("Select Target Column", df.columns)

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # ---------------------------
    # 4. Train Model
    # ---------------------------
    if st.button("Train Model"):

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        score = model.score(X_test, y_test)

        st.success(f"Model Trained Successfully 🎯 Accuracy Score: {score:.2f}")

        # ---------------------------
        # 5. Prediction Section
        # ---------------------------
        st.subheader("🔮 Make Prediction")

        input_data = []

        for col in X.columns:
            val = st.number_input(f"Enter value for {col}", value=0.0)
            input_data.append(val)

        if st.button("Predict"):
            prediction = model.predict([input_data])
            st.success(f"📊 Predicted Value: {prediction[0]}")