# training.py

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import joblib
import os

# =========================
# 📂 Load dataset
# =========================
df = pd.read_csv("Metro_Interstate_Traffic.csv")

print("Dataset loaded ✅")

# =========================
# 🧠 Preprocessing
# =========================

df["date_time"] =pd.to_datetime(df["date_time"])
df["hour"] = df["date_time"].dt.hour
df["day"] = df["date_time"].dt.dayofweek
df["month"] = df["date_time"].dt.month

# Target
def traffic_label(x):
    if x < 2000:
        return "Low"
    elif x < 4000:
        return "Medium"
    else:
        return "High"

df["traffic_level"] = df["traffic_volume"].apply(traffic_label)

# Features
X = df[["temp", "rain_1h", "snow_1h", "clouds_all", "hour", "day", "month"]]
y = df["traffic_level"]

# Clean missing
X = X.fillna(X.median())

# =========================
# 💾 Save Cleaned Data
# =========================
os.makedirs("data/processed", exist_ok=True)
df_cleaned = X.copy()
df_cleaned["traffic_level"] = y
df_cleaned.to_csv("data/processed/cleaned_traffic_data.csv", index=False)

print("Cleaned dataset saved ✅")

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
# 🤖 MODEL 1: Random Forest
# =========================
rf_model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

print(f"Random Forest Accuracy: {rf_acc:.2f}")

# =========================
# 🤖 MODEL 2: Logistic Regression
# =========================
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)

print(f"Logistic Regression Accuracy: {lr_acc:.2f}")

# =========================
# 📊 Cross Validation (PRO)
# =========================
rf_cv = cross_val_score(rf_model, X_scaled, y, cv=5).mean()
lr_cv = cross_val_score(lr_model, X_scaled, y, cv=5).mean()

print(f"RF Cross-val: {rf_cv:.2f}")
print(f"LR Cross-val: {lr_cv:.2f}")

# =========================
# 🏆 Choose Best Model
# =========================
if rf_acc > lr_acc:
    best_model = rf_model
    print("Best Model: Random Forest 🏆")
else:
    best_model = lr_model
    print("Best Model: Logistic Regression 🏆")

# =========================
# 💾 Save Model
# =========================
os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/traffic_model.joblib")
joblib.dump(scaler, "models/scaler.pkl")

print("Best model saved ✅")