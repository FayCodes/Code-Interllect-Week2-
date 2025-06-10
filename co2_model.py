# mporting libraries
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Loading the Excel file
file_path = "Mumias_Sugar_CO2_Emissions_10_Years.xlsx"
df = pd.read_excel(file_path)

# Previewing the data
print("First 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nSummary Stats:")
print(df.describe())

# Importing machine learning tools

# Selecting features and target
features = ['Energy_Consumption_kWh', 'Diesel_Usage_Liters',
            'Production_Output_Tons', 'Waste_Generated_Tons', 'Number_of_Employees']
target = 'Estimated_CO2_Emissions_Tons'

X = df[features]
y = df[target]

# Spliting data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initializing and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on test data
y_pred = model.predict(X_test)

# Evaluating the model
print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"R-squared Score: {r2_score(y_test, y_pred):.2f}")

# Printing model coefficients
print("\nModel Coefficients:")
for i, col in enumerate(features):
    print(f"{col}: {model.coef_[i]:.4f}")

# Importing libraries for visualization

# Predict using the trained model
y_pred = model.predict(X)

# Plot actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], y, label='Actual CO₂ Emissions', color='blue')
plt.plot(df['Date'], y_pred, label='Predicted CO₂ Emissions',
         color='red', linestyle='--')
plt.xlabel('Date')
plt.ylabel('CO₂ Emissions (Tons)')
plt.title('Actual vs. Predicted CO₂ Emissions Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
