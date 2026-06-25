import pandas as pd

# 1. Load the original data
df = pd.read_csv('demand_forecasting.csv')

# 2. Define the Mapping (The "LLM-Inspired" Logic)
weather_map = {'Sunny': 1.2, 'Cloudy': 1.0, 'Rainy': 0.9, 'Snowy': 0.8}
epidemic_map = {0: 1.0, 1: 0.6}

# 3. Create the new "Context Score" columns
df['Weather_Score'] = df['Weather Condition'].map(weather_map)
df['Epidemic_Score'] = df['Epidemic'].map(epidemic_map)

# 4. Save the new hybrid dataset
df.to_csv('demand_forecasting_hybrid.csv', index=False)

print("Hybrid dataset created: 'demand_forecasting_hybrid.csv'")
print(df[['Weather Condition', 'Weather_Score', 'Epidemic', 'Epidemic_Score']].head())