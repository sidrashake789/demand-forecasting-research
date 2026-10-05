"""Early experiment: 3-feature Random Forest evaluated with MAE (units) instead of MAPE."""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Set up path resolution assuming this script lives in the experiments/ directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "demand_forecasting.csv"

# 1. Load the raw dataset
df = pd.read_csv(RAW_DATA)

# 2. Select a small subset of features for a quick exploratory run
features = ['Inventory Level', 'Units Ordered', 'Price']
X = df[features]
y = df['Units Sold']

# 3. Split and train using a consistent random seed
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Use Mean Absolute Error (MAE) to check unit-level error variance
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)

print("Exploratory 3-Feature Random Forest Experiment Complete.")
print(f"Mean Absolute Error (MAE): {mae:.2f} units")