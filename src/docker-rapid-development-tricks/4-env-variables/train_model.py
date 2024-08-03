from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

import os

random_seed = int(os.getenv("RANDOM_SEED", 0))
c_reg_strength = float(os.getenv("C_REG_STRENGTH", 1))

print(f"random_seed: {random_seed}")
print(f"c_reg_strength: {c_reg_strength}")

X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=random_seed, C=c_reg_strength)
clf.fit(X, y)

print("Sample probabilities:")
print(clf.predict_proba(X[:2, :]))

print("Classifier score on training data:")
print(clf.score(X, y))
