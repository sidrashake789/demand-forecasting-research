import pandas as pd

df = pd.read_csv('demand_forecasting.csv')

# Check what type the 'Units Sold' column is
print("Data type of 'Units Sold':")
print(df['Units Sold'].dtype)

# Show the first 10 values
print("\nFirst 10 values:")
print(df['Units Sold'].head(10))

# Check for non-numeric values
print("\nAre there any non-numeric values?")
print(pd.to_numeric(df['Units Sold'], errors='coerce').isna().sum())