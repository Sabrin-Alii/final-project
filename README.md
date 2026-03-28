🚦 Traffic Prediction System

📌 Project Description

This project is a Machine Learning-based Traffic Prediction System that predicts traffic levels (Low, Medium, High) based on environmental and time-related data.

The system uses:

- FastAPI (Backend)
- React.js (Frontend)
- Machine Learning Model (Scikit-learn)

---

⚙️ Features

- Predict traffic level using input data
- User-friendly interface
- Real-time prediction
- Deployed online

---

🧠 Technologies Used

- Python
- FastAPI
- React.js
- Scikit-learn
- NumPy
- Joblib

---

📊 Input Parameters

- Temperature
- Rain (last 1 hour)
- Snow (last 1 hour)
- Cloud coverage
- Hour
- Day
- Month

---

🚀 How to Run Locally

Backend

uvicorn app:app --reload

Frontend

npm install
npm start


real-final/
│
├── app.py
├── traffic_model.joblib
├── scaler.pkl
├── requirements.txt
│
└── traffic-frontend/
    ├── src/
    ├── package.json
---

🌍 Live Demo

- Backend: https://traffic-backend-9ocq.onrender.com/
- Frontend: https://final-project-khaki-two.vercel.app/.app

---

🎓 Author

- Sabrin Ali Hussein

---

📌 Conclusion

This project demonstrates how machine learning can be integrated with web technologies to solve real-world problems like traffic prediction.
