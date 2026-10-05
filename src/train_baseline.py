"""Baseline model: Random Forest using only store sales and pricing info (no weather or health data)."""

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Figure out the root directory path so this runs smoothly from anywhere
ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = ROOT / "data" / "raw" / "demand_forecasting.csv"

# Load up the raw dataset
df = pd.read_csv(RAW_DATA)

# Pick out our baseline features (ignoring the new context scores)
features = ['Inventory Level', 'Units Ordered', 'Price', 'Discount', 'Competitor Pricing']
X = df[features].fillna(0)
y = df['Units Sold']

# Split into training and test sets (80/20 split, using random_state for consistency)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fire up the Random Forest model with 100 trees
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Generate predictions on the test set and make sure we don't have negative sales
predictions = model.predict(X_test)
predictions = np.maximum(predictions, 0.001)

# Calculate modified MAPE with epsilon = 1.0 to handle rows with zero sales gracefully
epsilon = 1.0
mape = np.mean(np.abs((y_test - predictions) / (y_test + epsilon))) * 100

print(f"Baseline Model MAPE (adjusted): {mape:.2f}%")