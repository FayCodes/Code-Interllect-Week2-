
import pandas as pd
import os

# Ensure 'data' folder exists
os.makedirs("data", exist_ok=True)

# Load dataset
df = pd.read_csv("data/Carbon_Emissions.csv")

# Filter for Kenya
df_kenya = df[df["Country"] == "Kenya"].copy()  # Explicitly create a copy to avoid warnings

# Extract Year from Date (Fix for SettingWithCopyWarning)
df_kenya.loc[:, "Year"] = pd.to_datetime(df_kenya["Date"]).dt.year

# Keep only relevant columns
df_kenya = df_kenya[["Year", "Kilotons of Co2"]]

# Rename columns for clarity
df_kenya.rename(columns={"Kilotons of Co2": "CO2 Emissions"}, inplace=True)

# Drop any missing values
df_kenya.dropna(inplace=True)

# Save the cleaned dataset
df_kenya.to_csv("data/kenya_emissions.csv", index=False)

print("✅ Preprocessed dataset saved as data/kenya_emissions.csv")

