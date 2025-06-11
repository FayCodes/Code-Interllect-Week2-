
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("models/linear_regression.pkl")

# Define future years for prediction
future_years = pd.DataFrame({"Year": [2025, 2030, 2040]})

# Make predictions
future_years["Predicted CO2 Emissions"] = model.predict(future_years)

# Save predictions
future_years.to_csv("data/future_predictions.csv", index=False)

print("✅ Future predictions saved as data/future_predictions.csv")
print(future_years)
