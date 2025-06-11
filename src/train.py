
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load cleaned dataset
df = pd.read_csv("data/kenya_emissions.csv")

# Define independent (X) and dependent (y) variables
X = df[["Year"]]  # Independent variable
y = df["CO2 Emissions"]  # Dependent variable

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/linear_regression.pkl")

print("✅ Linear Regression model trained and saved as models/linear_regression.pkl")
