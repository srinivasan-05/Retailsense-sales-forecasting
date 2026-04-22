# 🚀 RetailSense: Smart Sales & Inventory Forecasting System

## 📌 Project Overview
RetailSense is a machine learning-based web application developed using Streamlit that predicts retail sales and provides intelligent inventory decisions. The system helps businesses forecast future sales based on historical data and key influencing factors such as temperature, fuel price, CPI, unemployment, and seasonal trends.

The application not only predicts sales but also assists in decision-making by indicating whether stock levels are sufficient or if restocking is required.

---

## 🎯 Objectives
- Predict weekly retail sales using machine learning models
- Compare performance of different models
- Provide actionable business insights
- Assist in inventory management decisions
- Build an interactive and user-friendly dashboard

---

## ⚙️ Technologies Used
- **Python**
- **Streamlit** (for web app UI)
- **Pandas & NumPy** (data processing)
- **Scikit-learn** (ML models)
- **XGBoost** (advanced boosting model)
- **Matplotlib** (visualization)

---

## 📊 Machine Learning Models Used
1. **Linear Regression**
   - Basic model assuming linear relationships
   - Used for baseline comparison

2. **Random Forest Regressor**
   - Ensemble model using multiple decision trees
   - Captures complex relationships

3. **XGBoost Regressor**
   - Advanced boosting algorithm
   - Provides high accuracy and performance

---

## 📈 Features of the System
- 📁 Upload custom CSV dataset
- 📊 Data preview and visualization
- 📈 Sales trend analysis (store-wise)
- 📅 Monthly sales insights
- 🤖 Model performance comparison (R² Score)
- 🔮 Real-time sales prediction
- 📦 Inventory decision support (Restock / Sufficient)
- 🎛 Interactive input controls (sliders, dropdowns)
- 🎨 Modern and user-friendly dashboard

---

## 🧠 How It Works
1. User uploads a dataset
2. Data is preprocessed:
   - Date conversion
   - Feature extraction (Month, Year)
3. Machine learning models are trained
4. Model performance is evaluated using R² score
5. User inputs parameters (store, temperature, etc.)
6. Selected model predicts sales
7. System compares predicted sales with stock
8. Displays decision:
   - Restock Required
   - Stock is Sufficient

---

## 📊 Model Evaluation
The system evaluates models using the **R² Score**:
- ❌ Poor (< 0.4)
- ⚠️ Average (0.4 – 0.6)
- 🔥 Excellent (> 0.6)

This helps users understand model performance clearly.

---

## 💡 Key Insights
- Sales are influenced by seasonal trends and external factors
- Tree-based models (Random Forest, XGBoost) outperform linear models
- Inventory decisions can be optimized using predictions

---

## 🚀 Future Enhancements
- Train-test split for better generalization
- Hyperparameter tuning for improved accuracy
- Deployment on cloud (Streamlit Cloud / AWS)
- Real-time data integration
- Advanced visual dashboards

---

## ▶️ How to Run the Project

### 1. Clone the repository
git clone https://github.com/srinivasan-05/retailsense-sales-forecasting.git

### 2. Navigate to folder
cd retailsense-sales-forecasting

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
streamlit run app.py

---

## 👨‍💻 Conclusion
RetailSense demonstrates how machine learning can be applied to real-world retail problems. It provides a practical solution for sales forecasting and inventory management, helping businesses make data-driven decisions.
