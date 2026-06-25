import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_percentage_error

# Load the data
df = pd.read_csv('demand_forecasting.csv')

# Preprocessing: Convert categorical text data to numbers
# We drop non-numeric columns for the base model, but we will use them for the LLM part later
df_numeric = df.select_dtypes(include=['number'])

# Define target and features
target = 'Units Sold'
features = [col for col in df_numeric.columns if col != target]

X = df_numeric[features]
y = df_numeric[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = HistGradientBoostingRegressor()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mape = mean_absolute_percentage_error(y_test, predictions)

print(f"Model Training Complete.")
print(f"Mean Absolute Percentage Error (MAPE): {mape:.4f}")