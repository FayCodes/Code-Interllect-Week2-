# Code-Interllect-Week2-
Group repository — includes individual contributions on different SDG Projects

# AI-Assignment-Week2

## Kenya CO₂ Emissions Forecasting for Climate Action

### 👥 Group Members

Each team member explored a unique AI concept for this assignment. After internal peer review, the project in the `main` branch — focused on Kenya's CO₂ emissions — was voted by the group to represent our submission. Other individual contributions can be found in separate branches.

- **Faith Wafula** – *Selected Project Lead, Data Analysis & Modeling*
- **Patrick Obondo** 
- **Jeremiah Katumo** 
- **Naomi Wairimu** 
- **Eloga Pharix** 

---

### 🔹 Project Overview

This project aligns with **Sustainable Development Goal (SDG) 13: Climate Action**, using machine learning to forecast Kenya’s carbon emissions. By analyzing historical data, we aim to provide actionable insights that can support policymakers, industries, and environmental organizations in making data-driven decisions to reduce CO₂ output and implement sustainable policies.

---

### 🔹 Machine Learning Approach

The project implemented **Linear Regression**, a simple yet effective model for identifying long-term trends in emissions data. By training on historical CO₂ emissions, we forecast Kenya’s emissions for **2025**, **2030**, and **2040** — offering a strategic roadmap for climate policy planning.

---

### 🔹 Results Summary

| Year  | Predicted CO₂ Emissions (Kilotons) |
|-------|------------------------------------|
| 2025  | 21,090.73                          |
| 2030  | 23,661.43                          |
| 2040  | 28,802.84                          |

These projections emphasize the urgent need for sustainable development efforts.

---

### 🔹 Ethical Considerations

- ✔ **Data Accuracy**: Using reliable and publicly available emissions data.
- ✔ **Policy Impact**: Designed to inform sustainable policies, not manipulate them.
- ✔ **Bias & Fairness**: Acknowledging that linear models may oversimplify complex climate dynamics.

---

### 🔹 Document Arrangement

📂 data/ → Cleaned emissions dataset (kenya_emissions.csv)
📂 src/ → Codebase: data processing, training, prediction (train.py, predict.py)
📂 models/ → Serialized regression model (linear_regression.pkl)
📂 report/ → Full written report

yaml
Copy
Edit

📄 [Full Report (Google Docs)]( https://docs.google.com/document/d/1qlCjOBYlBZ10DlbCNMNSGRjxDrqul99hMeofAPtLxgM/edit?usp=sharing )

---

### 🔹 How to Run the Project

1️⃣ Install dependencies:
```bash
pip install -r requirements.txt
2️⃣ Run the prediction script:

bash
Copy
Edit
python src/predict.py
3️⃣ Forecasted emissions will be saved in:

bash
Copy
Edit
data/future_predictions.csv
🔹 Conclusion
This project demonstrates the power of machine learning in addressing climate challenges by providing a predictive view of CO₂ emissions. Future iterations may integrate more advanced time series models (e.g.,ARIMA,LSTM) and broader environmental data. Our goal is to continue building tools that guide informed and sustainable decision-making in Kenya and beyond.







