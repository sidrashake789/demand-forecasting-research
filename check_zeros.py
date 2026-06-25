import pandas as pd

df = pd.read_csv('demand_forecasting.csv')
zero_count = (df['Units Sold'] == 0).sum()
total_count = len(df)

print(f"Total rows: {total_count}")
print(f"Rows with 0 Units Sold: {zero_count}")