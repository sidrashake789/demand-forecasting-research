"""Hybrid model: Random Forest using both transactional features and our engineered context scores."""

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Point to the processed dataset that has the weather and epidemic scores added
ROOT = Path(__file__).resolve().parents[2]
HYBRID_DATA = ROOT / "data" / "processed" / "demand_forecasting_hybrid.csv"

# Load up the hybrid data table
df = pd.read_csv(HYBRID_DATA)

# Select features, swapping out discount/competitor pricing for our new context scores
features = ['Inventory Level', 'Units Ordered', 'Price', 'Weather_Score', 'Epidemic_Score']
X = df[features].fillna(0)
y = df['Units Sold']

# Split data using the exact same random seed so the test split is identical
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and compute the adjusted MAPE metric
predictions = model.predict(X_test)
epsilon = 1.0
mape = np.mean(np.abs((y_test - predictions) / (y_test + epsilon))) * 100

print(f"Hybrid Model MAPE (Adjusted): {mape:.2f}%")