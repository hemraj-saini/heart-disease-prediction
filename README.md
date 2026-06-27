# ❤️ Heart Disease Prediction using Machine Learning

## Live Demo

[🚀 Launch Application](https://heart-disease-3rd.streamlit.app/)
## Overview

This project predicts whether a patient has heart disease using machine learning. Multiple classification algorithms were compared, hyperparameter tuning was performed, and the best CatBoost model was deployed using Streamlit.

---

## Dataset

* Cleveland Heart Disease Dataset
* Binary Classification
* 13 Input Features
* 1 Target Variable

---

## Features

* Age
* Gender
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG Result
* Maximum Heart Rate
* Exercise Induced Angina
* ST Depression
* ECG Stress Test Result
* Number of Major Blood Vessels
* Thalassemia Test Result

---

## Project Workflow

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Selection
* Model Comparison
* Hyperparameter Tuning
* Model Evaluation
* Feature Importance Analysis
* Model Deployment using Streamlit

---

## Models Compared

| Model                | Balanced Accuracy |
| -------------------- | ----------------: |
| Extra Trees          |            0.8402 |
| CatBoost             |            0.8325 |
| Logistic Regression  |            0.8294 |
| Random Forest        |            0.8257 |
| HistGradientBoosting |            0.8213 |
| LightGBM             |            0.8032 |
| XGBoost              |            0.7861 |

---

## Final Model

**CatBoost Classifier**

### Test Performance

* Accuracy: **81.97%**
* Balanced Accuracy: **80.63%**
* Macro F1-Score: **0.81**

---

## Feature Importance

The most important features identified by CatBoost include:

* Chest Pain Type
* Thalassemia
* Number of Major Blood Vessels
* Oldpeak
* Slope

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* CatBoost
* Matplotlib
* Streamlit
* Joblib

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
streamlit run app.py
```

---

## Project Structure

```text
heart-disease-prediction/
│
├── app.py
├── best_model.joblib
├── Heart_Disease.ipynb
├── heart_disease_data.csv
├── requirements.txt
└──  README.md
```

---

## Author

Hemraj Saini
