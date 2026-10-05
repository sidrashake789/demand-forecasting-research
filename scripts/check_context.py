"""Sanity check: unique values in the weather and epidemic columns."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "demand_forecasting.csv"


df = pd.read_csv(RAW_DATA)

# Look at the unique categories in your context columns
print("Weather Conditions:")
print(df['Weather Condition'].unique())

print("\nEpidemic Status:")
print(df['Epidemic'].unique())