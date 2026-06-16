import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# Load Model
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "gradient_boosting_model.pkl"

model = joblib.load(MODEL_PATH)

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Online Shopper Intent Radar",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Online Shopper Intent Radar")

st.markdown(
"""
Predict whether an online shopping session is likely
to result in a purchase using a trained Machine Learning model.
"""
)

st.divider()

# -----------------------------
# Inputs
# -----------------------------

product_related = st.number_input(
    "Product Related Pages",
    min_value=1,
    value=25
)

product_duration = st.number_input(
    "Product Related Duration",
    min_value=0.0,
    value=500.0
)

bounce_rate = st.number_input(
    "Bounce Rate",
    min_value=0.0,
    value=0.02,
    format="%.4f"
)

exit_rate = st.number_input(
    "Exit Rate",
    min_value=0.0,
    value=0.05,
    format="%.4f"
)

page_values = st.number_input(
    "Page Value",
    min_value=0.0,
    value=15.0
)

month = st.selectbox(
    "Month",
    ["Feb","Mar","May","June","Jul","Aug","Sep","Oct","Nov","Dec"]
)

visitor = st.selectbox(
    "Visitor Type",
    ["Returning_Visitor","New_Visitor","Other"]
)

weekend = st.selectbox(
    "Weekend",
    [False,True]
)

# -----------------------------
# Predict
# -----------------------------

if st.button("Predict Purchase Intent"):

    sample = pd.DataFrame({

        "Administrative":[2],
        "Administrative_Duration":[30],

        "Informational":[1],
        "Informational_Duration":[10],

        "ProductRelated":[product_related],
        "ProductRelated_Duration":[product_duration],

        "BounceRates":[bounce_rate],
        "ExitRates":[exit_rate],

        "PageValues":[page_values],

        "SpecialDay":[0],

        "Month":[month],

        "OperatingSystems":[2],

        "Browser":[2],

        "Region":[1],

        "TrafficType":[2],

        "VisitorType":[visitor],

        "Weekend":[weekend]

    })

    probability = model.predict_proba(sample)[0][1]

    prediction = model.predict(sample)[0]

    st.divider()

    st.subheader("Prediction")

    st.metric(
        "Purchase Probability",
        f"{probability*100:.2f}%"
    )

    if prediction:

        st.success("✅ Likely to Purchase")

    else:

        st.error("❌ Unlikely to Purchase")