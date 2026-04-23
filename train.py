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