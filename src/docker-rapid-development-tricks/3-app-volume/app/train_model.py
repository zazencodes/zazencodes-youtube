import pandas as pd
from sklearn.linear_model import LinearRegression
from pickle import dump

# Load data
data = pd.read_csv("/data/input_data.csv")

# Train model
X = data[["x1", "x2"]]
y = data["y"]
model = LinearRegression()
model.fit(X, y)

# Save model
with open("/artifacts/linear_regression_model.pkl", "wb") as f:
    dump(model, f)
