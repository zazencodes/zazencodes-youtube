from pickle import load

import sys

args = sys.argv[1:]
if len(args) != 2:
    raise ValueError("Must pass two arguments, i.e. python run_model.py x1 x2")

x1, x2 = int(args[0]), int(args[1])

with open("/artifacts/linear_regression_model.pkl", "rb") as f:
    model = load(f)

y_pred = model.predict([[x1, x2]])[0]
print(f"Predicted y = {y_pred:.2f} for (x1 = {x1:.2f}, x2 = {x2:.2f})")
