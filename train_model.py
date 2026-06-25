import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error

# 1. Load data
df = pd.read_csv('demand_forecasting.csv')

# 2. Prepare features (using numeric columns that correlate with sales)
features = ['Inventory Level', 'Units Ordered', 'Price', 'Discount', 'Competitor Pricing']
X = df[features].fillna(0)
y = df['Units Sold']

# 3. Split and Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Generate Forecasts
predictions = model.predict(X_test)

# Sanity Check: Predictions should not be negative
predictions = np.maximum(predictions, 0.001) 
# ... (keep your existing model training and prediction lines)

# 4. Generate Forecasts
predictions = model.predict(X_test)

# 5. Standard MAPE with Epsilon Adjustment
# We add 1.0 to the denominator to prevent the "division by zero" 
# or "small denominator" explosion.
epsilon = 1.0 
mape = np.mean(np.abs((y_test - predictions) / (y_test + epsilon))) * 100

print(f"Standard MAPE (adjusted): {mape:.2f}%")