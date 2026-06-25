import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# 1. Load your NEW hybrid data
df = pd.read_csv('demand_forecasting_hybrid.csv')

# 2. Add the new features to your model's inputs
features = ['Inventory Level', 'Units Ordered', 'Price', 'Weather_Score', 'Epidemic_Score']
X = df[features].fillna(0)
y = df['Units Sold']

# 3. Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Predict and Calculate (Using the same Epsilon approach)
predictions = model.predict(X_test)
epsilon = 1.0
mape = np.mean(np.abs((y_test - predictions) / (y_test + epsilon))) * 100

print(f"--- Hybrid Model Performance ---")
print(f"Standard MAPE (Adjusted): {mape:.2f}%")