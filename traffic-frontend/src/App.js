import React, { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    temp: "",
    rain_1h: "",
    snow_1h: "",
    clouds_all: "",
    hour: "",
    day: "",
    month: "",
  });

  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch("https://traffic-backend-9ocq.onrender.com/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          temp: Number(formData.temp || 0),
          rain_1h: Number(formData.rain_1h || 0),
          snow_1h: Number(formData.snow_1h || 0),
          clouds_all: Number(formData.clouds_all || 0),
          hour: Number(formData.hour || 0),
          day: Number(formData.day || 0),
          month: Number(formData.month || 0),
        }),
      });

      // 🔥 HANDLE ERROR
      if (!response.ok) {
        const text = await response.text();
        console.error("Backend Error:", text);
        setResult("Server Error ❌");
        return;
      }

      const data = await response.json();
      setResult(data.prediction);

    } catch (error) {
      console.error("Fetch Error:", error);
      setResult("Server Error ❌");
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1>🚦 Traffic Prediction</h1>

        {/* NUMBER INPUTS */}
        <input type="number" name="temp" placeholder="Temperature (°C)" onChange={handleChange} />
        <input type="number" name="rain_1h" placeholder="Rain (1h)" onChange={handleChange} />
        <input type="number" name="snow_1h" placeholder="Snow (1h)" onChange={handleChange} />
        <input type="number" name="clouds_all" placeholder="Clouds (%)" onChange={handleChange} />

        {/* SELECT DROPDOWNS */}
        <select name="hour" onChange={handleChange}>
          <option value="">Select Hour</option>
          {[...Array(24).keys()].map(h => (
            <option key={h} value={h}>{h}:00</option>
          ))}
        </select>

        <select name="day" onChange={handleChange}>
          <option value="">Select Day</option>
          {[...Array(31).keys()].map(d => (
            <option key={d+1} value={d+1}>{d+1}</option>
          ))}
        </select>

        <select name="month" onChange={handleChange}>
          <option value="">Select Month</option>
          {[...Array(12).keys()].map(m => (
            <option key={m+1} value={m+1}>{m+1}</option>
          ))}
        </select>

        <button onClick={handleSubmit}>Predict</button>

        {result && <h2>Result: {result}</h2>}
      </div>
    </div>
  );
}

 export default App;