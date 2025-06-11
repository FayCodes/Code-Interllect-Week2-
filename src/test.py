
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score

# Load cleaned dataset
df = pd.read_csv("data/kenya_emissions.csv")

# Load trained model
model = joblib.load("models/linear_regression.pkl")

# Define independent (X) and dependent (y) variables
X = df[["Year"]]
y = df["CO2 Emissions"]

# Make predictions
y_pred = model.predict(X)

# Evaluate model performance
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"✅ Model Evaluation Results:")
print(f"🔹 Mean Absolute Error (MAE): {mae:.2f}")
print(f"🔹 R² Score: {r2:.4f}")

# Plot actual vs. predicted emissions
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Actual Emissions")
plt.plot(X, y_pred, color="red", linestyle="dashed", label="Predicted Trend")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (Kilotons)")
plt.title("Kenya CO2 Emissions Forecast (Linear Regression)")
plt.legend()
plt.grid(True)
plt.show()
