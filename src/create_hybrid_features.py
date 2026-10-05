"""Build the context-aware (hybrid) dataset: maps weather and epidemic status to numeric scores."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = ROOT / "data" / "raw" / "demand_forecasting.csv"
HYBRID_DATA = ROOT / "data" / "processed" / "demand_forecasting_hybrid.csv"


# 1. Load the original data
df = pd.read_csv(RAW_DATA)

# 2. Define the Mapping (The "LLM-Inspired" Logic)
weather_map = {'Sunny': 1.2, 'Cloudy': 1.0, 'Rainy': 0.9, 'Snowy': 0.8}
epidemic_map = {0: 1.0, 1: 0.6}

# 3. Create the new "Context Score" columns
df['Weather_Score'] = df['Weather Condition'].map(weather_map)
df['Epidemic_Score'] = df['Epidemic'].map(epidemic_map)

# 4. Save the new hybrid dataset
HYBRID_DATA.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(HYBRID_DATA, index=False)

print(f"Hybrid dataset created: {HYBRID_DATA.relative_to(ROOT)}")
print(df[['Weather Condition', 'Weather_Score', 'Epidemic', 'Epidemic_Score']].head())