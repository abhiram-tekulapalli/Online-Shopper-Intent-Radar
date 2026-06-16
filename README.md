# 🛒 Online Shopper Intent Radar

An end-to-end Machine Learning project that predicts whether an online shopping session is likely to result in a purchase based on user browsing behavior.

---

## 📌 Project Overview

E-commerce platforms generate thousands of user sessions every day, but only a small percentage lead to purchases.

This project analyzes user browsing patterns and predicts purchase intent using Machine Learning, enabling businesses to identify high-conversion sessions and improve marketing strategies.

---

## 🎯 Problem Statement

Predict whether an online shopping session will result in a purchase using historical user behavior data.

---

## 📊 Dataset

- **Dataset:** Online Shoppers Purchasing Intention Dataset
- **Source:** UCI Machine Learning Repository
- **Records:** 12,330 sessions
- **Features:** 17
- **Target Variable:** Revenue (Purchase / No Purchase)

---

## 🚀 Features

- Exploratory Data Analysis (EDA)
- Data Preprocessing Pipeline
- Multiple ML Model Comparison
- Gradient Boosting Classifier
- Feature Importance Analysis
- Interactive Streamlit Web Application
- Business Interpretation of Predictions

---

## 🛠️ Technologies Used

| Category | Technology |
|------------|----------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Deployment | Streamlit |
| Model Serialization | Joblib |

---

## 📈 Model Performance

| Model | Accuracy | ROC-AUC |
|----------------------|------------|-----------|
| Logistic Regression | 88.96% | 89.64% |
| KNN | 88.37% | 81.17% |
| Random Forest | 90.24% | 92.70% |
| **Gradient Boosting** | **90.60%** | **93.36%** |

---

## 📂 Project Structure

```
Online-Shopper-Intent-Radar/

│
├── app/
│     app.py
│
├── data/
│     raw/
│
├── models/
│     gradient_boosting_model.pkl
│
├── notebooks/
│     01_Online_Shopper_Intent_Radar.ipynb
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd Online-Shopper-Intent-Radar

pip install -r requirements.txt

streamlit run app/app.py
```

---

## 💻 Streamlit Application

The application allows users to:

- Enter browsing session information
- Predict purchase intent
- View purchase probability
- Receive business insights

---

## 📊 Business Impact

This system can help e-commerce companies:

- Identify high-value customers
- Improve conversion rates
- Personalize recommendations
- Optimize marketing campaigns

---

## 🔮 Future Scope

- Real-time prediction API
- Deep Learning implementation
- Customer segmentation integration
- Explainable AI using SHAP values

---

## 👨‍💻 Author

Tekulapalli Abhiram 
BVRIT Narsapur

Machine Learning Mini Project

Online Shopper Intent Radar