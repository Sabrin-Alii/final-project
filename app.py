from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
from fastapi.middleware.cors import CORSMiddleware

# 🚀 1. Create FastAPI App
app = FastAPI()

# 🛡️ 2. Enable CORS (Si Frontend-ka u shaqeeyo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 3. Load Model and Scaler
# Hubi in faylashan ay ku dhex jiraan folder-ka "models"
try:
    model = joblib.load("models/traffic_model.joblib")
    scaler = joblib.load("models/scaler.pkl")
    print("Model and Scaler loaded successfully! ✅")
except Exception as e:
    print(f"Error loading files: {e} ❌")

# 📥 4. Request Schema (7 Features)
class TrafficInput(BaseModel):
    temp: float
    rain_1h: float
    snow_1h: float
    clouds_all: float
    hour: int
    day: int
    month: int

# 🏠 5. Home Route
@app.get("/")
def home():
    return {"message": "Traffic Prediction API is Running! 🚀"}

# 🎯 6. Prediction Route
@app.post("/predict")
def predict(data: TrafficInput):
    try:
        # 🔢 Features Array (Gali dhamaan 7-da shay)
        features = np.array([[
            data.temp,
            data.rain_1h,
            data.snow_1h,
            data.clouds_all,
            data.hour,
            data.day,
            data.month
        ]])

        # ⚖️ Scale Data
        scaled_features = scaler.transform(features)

        # 🤖 Model Prediction
        # Model-kaagu wuxuu soo celinayaa String ("High", "Medium", "Low")
        prediction = model.predict(scaled_features)[0]

        # 📤 Return Natiijada toos ah
        return {"prediction": str(prediction)}

    except Exception as e:
        print(f"Prediction Error: {e}")
        return {"prediction": f"Server Error: {str(e)} ❌"}

# 🚀 7. Run Command (Isticmaal kan terminal-ka):
# uvicorn app:app --reload