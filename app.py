<<<<<<< HEAD
=======

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

        # 5. Prediction Section
        st.subheader("🔮 Make Prediction")

        input_data = []

        for col in X.columns:
            val = st.number_input(f"Enter value for {col}", value=0.0)
            input_data.append(val)

        if st.button("Predict"):
            prediction = model.predict([input_data])
            st.success(f"📊 Predicted Value: {prediction[0]}")
>>>>>>> 0cd7246 (add model file)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 📌 Step 1: Load Data
data = pd.read_csv("data.csv")

print("Data Preview:\n", data.head())
print("\nColumns:\n", data.columns)

# 📌 Step 2: Remove Date column (if exists)
for col in data.columns:
    if 'date' in col.lower():
        data = data.drop(col, axis=1)

# 📌 Step 3: Auto detect target column (price/close)
target_column = None

for col in data.columns:
    if 'close' in col.lower() or 'price' in col.lower():
        target_column = col
        break

# ❌ agar target na mile
if target_column is None:
    raise Exception("❌ No price/close column found! Apni CSV check karo")

print("\n✅ Using target column:", target_column)

data = data.select_dtypes(include=[np.number])
data = data.dropna()

# 📌 Step 4: Features & Target
X = data.drop([target_column], axis=1)
y = data[target_column]

# 📌 Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 📌 Step 6: Model (Advanced)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# 📌 Step 7: Prediction
y_pred = model.predict(X_test)

# 📌 Step 8: Accuracy
mse = mean_squared_error(y_test, y_pred)
print("\n📊 Mean Squared Error:", mse)

# 📌 Step 9: Graph
plt.figure(figsize=(10,5))
plt.plot(y_test.values, label="Actual")
plt.plot(y_pred, label="Predicted")
plt.legend()
plt.title("Stock Price Prediction")
plt.show()
import streamlit as st
import pickle

# 🔥 UI (ye missing tha)
st.title("Stock Price Prediction App 🚀")
st.write("Model is running successfully")

# Model load
model = pickle.load(open("model.pkl", "rb"))

# Input
value = st.number_input("Enter turnover value")

# Button
if st.button("Predict"):
    result = model.predict([[value]])
<<<<<<< HEAD
    st.success(f"Prediction: {result[0]}")
=======
    st.success(f"Prediction: {result[0]}")
>>>>>>> 0cd7246 (add model file)
