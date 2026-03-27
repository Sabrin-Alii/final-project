# train.py

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib
import os

# 📂 Load dataset
df = pd.read_csv("Metro_Interstate_Traffic.csv")

print("Dataset loaded ✅")

# =========================
# 🧠 Feature Engineering
# =========================

# Convert date_time → hour
df["date_time"] = pd.to_datetime(df["date_time"])
df["hour"] = df["date_time"].dt.hour

# Create traffic level (TARGET)
def traffic_label(x):
    if x < 2000:
        return "Low"
    elif x < 4000:
        return "Medium"
    else:
        return "High"

df["traffic_level"] = df["traffic_volume"].apply(traffic_label)

# =========================
# 🧠 Feature Engineering
# =========================

# Convert date_time to datetime object
df["date_time"] = pd.to_datetime(df["date_time"])

# Extract 7 features
df["hour"] = df["date_time"].dt.hour
df["day"] = df["date_time"].dt.dayofweek
df["month"] = df["date_time"].dt.month

# Target Labeling
def traffic_label(x):
    if x < 2000:
        return "Low"
    elif x < 4000:
        return "Medium"
    else:
        return "High"

df["traffic_level"] = df["traffic_volume"].apply(traffic_label)

# =========================
# 🎯 Features (7 Inputs)
# =========================

# Make sure these column names match your CSV exactly
X = df[["temp", "rain_1h", "snow_1h", "clouds_all", "hour", "day", "month"]]
y = df["traffic_level"]

# Handle missing values
X = X.fillna(X.median())

# Handle missing
X = X.fillna(X.median())

# =========================
# ⚙️ Scaling
# =========================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# ✂️ Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# =========================
# 🤖 Model
# =========================

model = RandomForestClassifier()
model.fit(X_train, y_train)

# =========================
# 📊 Evaluation
# =========================

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy: {acc:.2f}")

# =========================
# 💾 Save
# =========================

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/traffic_model.joblib")
joblib.dump(scaler, "models/scaler.pkl")

print("Model saved ✅")