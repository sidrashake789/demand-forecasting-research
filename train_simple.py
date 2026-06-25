import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Load the data
df = pd.read_csv('demand_forecasting.csv')

# 2. Select a subset of features
features = ['Inventory Level', 'Units Ordered', 'Price']
X = df[features]
y = df['Units Sold']

# 3. Train and Evaluate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Use Mean Absolute Error (MAE) instead of MAPE to see actual unit error
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)

print(f"Mean Absolute Error (MAE): {mae:.2f} units")