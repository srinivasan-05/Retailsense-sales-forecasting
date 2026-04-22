import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="RetailSense Dashboard", layout="wide")

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
h1 {
    color: #00FFAA;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 RetailSense: Smart Sales & Inventory Dashboard")

# ---------- FILE UPLOAD ----------
uploaded_file = st.sidebar.file_uploader("📁 Upload Dataset", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # ---------- PREPROCESS ----------
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    features = ['Store','Holiday_Flag','Temperature','Fuel_Price','CPI','Unemployment','Month','Year']
    X = df[features]
    y = df['Weekly_Sales']

    # ---------- MODELS ----------
    lr = LinearRegression()
    rf = RandomForestRegressor(n_estimators=50)
    xgb = XGBRegressor(n_estimators=50, max_depth=5)

    lr.fit(X, y)
    rf.fit(X, y)
    xgb.fit(X, y)

    lr_score = r2_score(y, lr.predict(X))
    rf_score = r2_score(y, rf.predict(X))
    xgb_score = r2_score(y, xgb.predict(X))

    # ---------- SCORE VERDICT FUNCTION ----------
    def verdict(score):
        if score < 0.4:
            return "❌ Poor"
        elif score < 0.6:
            return "⚠️ Average"
        else:
            return "🔥 Excellent"

    # ---------- MODEL COMPARISON ----------
    st.subheader("📊 Model Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric("Linear Regression", f"{lr_score:.2f}", verdict(lr_score))
    col2.metric("Random Forest", f"{rf_score:.2f}", verdict(rf_score))
    col3.metric("XGBoost", f"{xgb_score:.2f}", verdict(xgb_score))

    # ---------- GRAPH SECTION ----------
    st.subheader("📈 Sales Insights")

    col1, col2 = st.columns(2)

    # Trend Graph
    with col1:
        store_graph = st.selectbox("Select Store for Trend", sorted(df['Store'].unique()))
        temp_df = df[df['Store'] == store_graph].sort_values("Date")

        fig1, ax1 = plt.subplots()
        ax1.plot(temp_df['Date'], temp_df['Weekly_Sales'], color='cyan')
        ax1.set_title("Sales Trend")
        st.pyplot(fig1)

    # Monthly Graph
    with col2:
        monthly = df.groupby('Month')['Weekly_Sales'].mean()

        fig2, ax2 = plt.subplots()
        ax2.bar(monthly.index, monthly.values, color='orange')
        ax2.set_title("Monthly Sales")
        st.pyplot(fig2)

    # ---------- SIDEBAR INPUT ----------
    st.sidebar.header("🎛 Input Parameters")

    model_choice = st.sidebar.selectbox("Choose Model", ["XGBoost", "Random Forest", "Linear Regression"])

    store = st.sidebar.selectbox("Store", sorted(df['Store'].unique()))
    holiday = st.sidebar.selectbox("Holiday Flag", [0, 1])
    temp = st.sidebar.slider("Temperature", 0.0, 50.0, 25.0)
    fuel = st.sidebar.slider("Fuel Price", 1.0, 5.0, 2.5)
    cpi = st.sidebar.slider("CPI", 100.0, 300.0, 200.0)
    unemp = st.sidebar.slider("Unemployment", 0.0, 15.0, 7.0)
    month = st.sidebar.slider("Month", 1, 12, 6)
    year = st.sidebar.slider("Year", 2010, 2025, 2012)
    stock = st.sidebar.number_input("Current Stock", value=1000000.0)

    # ---------- PREDICTION ----------
    st.subheader("🔮 Sales Prediction")

    if st.button("Predict Sales"):

        sample = pd.DataFrame([{
            'Store': store,
            'Holiday_Flag': holiday,
            'Temperature': temp,
            'Fuel_Price': fuel,
            'CPI': cpi,
            'Unemployment': unemp,
            'Month': month,
            'Year': year
        }])

        if model_choice == "Random Forest":
            pred = rf.predict(sample)
        elif model_choice == "Linear Regression":
            pred = lr.predict(sample)
        else:
            pred = xgb.predict(sample)

        st.success(f"💰 Predicted Sales: ₹ {pred[0]:,.2f}")

        # ---------- DECISION ----------
        if pred[0] > stock:
            st.error("⚠️ Restock Required")
        else:
            st.success("✅ Stock is sufficient")

        # ---------- BUSINESS INSIGHT ----------
        st.info("📌 Insight: Sales are influenced by seasonality, store location, and economic factors.")