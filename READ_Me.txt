# 📊 Medical Appointment No-Show Prediction & Demand Forecasting

This project is a machine learning system that helps in analyzing hospital appointment data to:
- Predict whether a patient will **show up or miss an appointment**
- Forecast **future appointment demand**
- Perform **exploratory data analysis (EDA)** to understand patient behavior patterns

It helps healthcare providers reduce no-shows and improve scheduling efficiency.

---

## 📁 Project Structure


---

## 🎯 Project Objectives

- Analyze patient appointment data
- Identify key factors affecting no-shows
- Build machine learning models for prediction
- Forecast future appointment demand
- Deploy a simple prediction interface

---

## 📊 Exploratory Data Analysis (EDA)

The `EDA.ipynb` notebook focuses on:
- Data cleaning and preprocessing
- Visualizing no-show patterns
- Understanding patient demographics
- Finding correlations between features

---

## 🤖 Machine Learning Models

### 🔹 No-Show Prediction Model
- Predicts whether a patient will attend an appointment
- Classification-based ML model
- Saved as `no_show_model.pkl`
- Includes preprocessing pipeline: `no_show_pipeline.pkl`

### 🔹 Demand Forecasting Model
- Predicts future appointment demand
- Helps in hospital resource planning
- Saved as `forecast_model.pkl`

---

## 🧠 Machine Learning Workflow

1. Data Collection (`data.csv`)
2. Data Preprocessing
3. Exploratory Data Analysis (`EDA.ipynb`)
4. Feature Engineering
5. Model Training
6. Model Saving (`.pkl` files)
7. Deployment using `app.py`

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook
- Pickle (model serialization)  