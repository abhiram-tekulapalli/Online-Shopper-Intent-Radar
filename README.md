# Online Shopper Intent Radar

<p align="center">
  <img src="https://raw.githubusercontent.com/abhiram-tekulapalli/project_readme_assets/main/header.svg" alt="Online Shopper Intent Radar" width="100%" />
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://scikit-learn.org"><img src="https://img.shields.io/badge/Scikit--Learn-1.5+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"></a>
  <a href="https://pandas.pydata.org"><img src="https://img.shields.io/badge/Pandas-2.2+-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"></a>
  <a href="https://numpy.org"><img src="https://img.shields.io/badge/NumPy-1.26+-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"></a>
  <a href="https://matplotlib.org"><img src="https://img.shields.io/badge/Matplotlib-3.9+-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"></a>
  <a href="https://seaborn.pydata.org"><img src="https://img.shields.io/badge/Seaborn-0.13+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn"></a>
  <a href="https://streamlit.io"><img src="https://img.shields.io/badge/Streamlit-1.38+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset"><img src="https://img.shields.io/badge/Dataset-UCI%20ML%20Repo-orange?style=for-the-badge" alt="UCI Dataset"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License"></a>
</p>

---

## 🎯 Overview

An end-to-end **Machine Learning project** that predicts whether an online shopping session will result in a purchase based on user browsing behavior. E-commerce platforms generate thousands of sessions daily, but only a small fraction convert — this project identifies high-intent sessions to improve marketing strategies and conversion rates.

---

## 📌 Problem Statement

> **Predict purchase intent** (Revenue: `True`/`False`) from historical user browsing behavior data to enable targeted interventions and personalized experiences.

---

## 📊 Dataset

| Attribute | Details |
|-----------|---------|
| **Name** | Online Shoppers Purchasing Intention Dataset |
| **Source** | [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset) |
| **Records** | 12,330 sessions |
| **Features** | 17 (10 numerical, 7 categorical) |
| **Target** | `Revenue` — Purchase (`True`) / No Purchase (`False`) |
| **Class Balance** | ~15.5% Positive (Purchase) |

### Key Features

| Category | Features |
|----------|----------|
| **Page Metrics** | Administrative, Administrative_Duration, Informational, Informational_Duration, ProductRelated, ProductRelated_Duration |
| **Rate Metrics** | BounceRates, ExitRates, PageValues |
| **Special Day** | SpecialDay (proximity to holidays) |
| **Temporal** | Month, OperatingSystems, Browser, Region, TrafficType |
| **User Type** | VisitorType (New/Returning/Other), Weekend (True/False) |

---

## 🚀 Features

- 📊 **Exploratory Data Analysis** — Distributions, correlations, class imbalance analysis
- 🔧 **Preprocessing Pipeline** — Encoding, scaling, train/test split, class balancing (SMOTE/undersampling)
- 🤖 **Multiple Model Comparison** — Logistic Regression, KNN, Random Forest, Gradient Boosting
- 🏆 **Gradient Boosting Classifier** — Best performing model (90.60% accuracy, 93.36% ROC-AUC)
- 📈 **Feature Importance Analysis** — SHAP/permutation importance for business interpretability
- 🌐 **Interactive Streamlit Web App** — Real-time prediction with probability scores
- 💼 **Business Interpretation** — Actionable insights for marketing & UX teams

---

## 📈 Model Performance

| Model | Accuracy | ROC-AUC | Precision | Recall | F1-Score |
|-------|----------|---------|-----------|--------|----------|
| Logistic Regression | 88.96% | 89.64% | 0.72 | 0.41 | 0.52 |
| KNN | 88.37% | 81.17% | 0.68 | 0.38 | 0.49 |
| Random Forest | 90.24% | 92.70% | 0.78 | 0.52 | 0.62 |
| **Gradient Boosting** | **90.60%** | **93.36%** | **0.81** | **0.55** | **0.66** |

> **Gradient Boosting** selected as production model — best balance of precision/recall for imbalanced data.

---

## 📂 Project Structure

```
Online-Shopper-Intent-Radar/
├── app/
│   └── app.py                 # Streamlit application
├── data/
│   └── raw/                   # Original dataset
├── models/
│   └── gradient_boosting_model.pkl  # Trained model artifact
├── notebooks/
│   └── 01_Online_Shopper_Intent_Radar.ipynb  # Full EDA + modeling
├── screenshots/               # App screenshots
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Usage

### Prerequisites
- Python 3.11+
- pip / conda

### Quick Start

```bash
# Clone repository
git clone https://github.com/abhiram-tekulapalli/Online-Shopper-Intent-Radar.git
cd Online-Shopper-Intent-Radar

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit app
streamlit run app/app.py
```

Open **http://localhost:8501** — enter session features → get purchase probability + business insights.

---

## 💻 Streamlit Application

The web app allows you to:

- 📝 **Input Session Data** — 17 feature fields with validation & tooltips
- 🎯 **Predict Purchase Intent** — Binary classification + probability score
- 📊 **View Probability Gauge** — Visual confidence indicator
- 💡 **Receive Business Insights** — Actionable recommendations per prediction
- 🔍 **Explore Feature Impact** — See which factors drove the decision

---

## 📊 Business Impact

| Use Case | Value |
|----------|-------|
| **High-Value Customer ID** | Target retention offers to likely converters |
| **Conversion Optimization** | Personalize UX for high-intent sessions |
| **Marketing Spend Efficiency** | Retarget high-probability abandoners |
| **Real-time Personalization** | Dynamic content/product recommendations |

---

## 🔮 Future Scope

- [ ] Real-time prediction API (FastAPI/Flask)
- [ ] Deep Learning implementation (TabNet, MLP)
- [ ] Customer segmentation integration (RFM + intent)
- [ ] Explainable AI with SHAP values
- [ ] A/B testing framework for interventions
- [ ] Model monitoring & drift detection

---

## 🛠️ Technologies

<div align="center">

| Category | Tools |
|----------|-------|
| **Language** | Python 3.11+ |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn (GradientBoostingClassifier, RandomForest, etc.) |
| **Deployment** | Streamlit |
| **Serialization** | Joblib |

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Tekulapalli Abhiram**  
BVRIT Narsapur — Computer Science & Engineering (AI/ML)  
[@abhiram-tekulapalli](https://github.com/abhiram-tekulapalli)

---

<p align="center">
  <img src="https://raw.githubusercontent.com/abhiram-tekulapalli/project_readme_assets/main/footer.svg" alt="Footer" width="100%" />
</p>