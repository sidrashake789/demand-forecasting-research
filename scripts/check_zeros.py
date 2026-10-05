"""Sanity check: how many rows have zero 'Units Sold' (motivates the MAPE epsilon)."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "demand_forecasting.csv"


df = pd.read_csv(RAW_DATA)
zero_count = (df['Units Sold'] == 0).sum()
total_count = len(df)

print(f"Total rows: {total_count}")
print(f"Rows with 0 Units Sold: {zero_count}")