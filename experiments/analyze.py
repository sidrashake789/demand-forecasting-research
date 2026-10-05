"""Early experiment: HistGradientBoosting with sklearn's MAPE (note: standard sklearn MAPE can be unstable when Units Sold is 0)."""

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_percentage_error

# Set up path resolution assuming this script lives in the experiments/ directory
ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "demand_forecasting.csv"

# Load up the raw dataset
df = pd.read_csv(RAW_DATA)

# Preprocessing: Select numerical columns for our exploratory baseline model
df_numeric = df.select_dtypes(include=['number'])

# Define target variable and feature set
target = 'Units Sold'
features = [col for col in df_numeric.columns if col != target]

X = df_numeric[features]
y = df_numeric[target]

# Split data using the same consistent random seed
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an exploratory HistGradientBoosting model
model = HistGradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate using standard sklearn MAPE
predictions = model.predict(X_test)
mape = mean_absolute_percentage_error(y_test, predictions)

print("Exploratory HistGradientBoosting Experiment Complete.")
print(f"Standard Mean Absolute Percentage Error (MAPE): {mape:.4f}")