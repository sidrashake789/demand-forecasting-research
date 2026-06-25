import pandas as pd

df = pd.read_csv('demand_forecasting.csv')

# Look at the unique categories in your context columns
print("Weather Conditions:")
print(df['Weather Condition'].unique())

print("\nEpidemic Status:")
print(df['Epidemic'].unique())