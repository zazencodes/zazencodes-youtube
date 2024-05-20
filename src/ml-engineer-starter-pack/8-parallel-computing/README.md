# Parallel computing

## Basic demo

- [ ] Run `demo.py`
- [ ] Observe htop processes being spawned (filter on python)
- [ ] Compare with `NUM_CORES = 1`


## ML demo

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time

INFLATE_FACTOR = 10000

# Load the iris dataset
data = load_iris()
X = np.concatenate([data.data for _ in range(INFLATE_FACTOR)])
y = np.concatenate([data.target for _ in range(INFLATE_FACTOR)])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the RandomForestClassifier with parallel processing
rf_parallel = RandomForestClassifier(n_jobs=-1, random_state=42)

# Measure the training time for parallel processing
start_time = time.time()
rf_parallel.fit(X_train, y_train)
parallel_duration = time.time() - start_time

# Predict and calculate accuracy
y_pred_parallel = rf_parallel.predict(X_test)
accuracy_parallel = accuracy_score(y_test, y_pred_parallel)

# Output the results for parallel processing
print(f"Parallel training time: {parallel_duration:.4f} seconds")
print(f"Parallel accuracy: {accuracy_parallel:.4f}")

# Initialize the RandomForestClassifier without parallel processing (single core)
rf_serial = RandomForestClassifier(n_jobs=1, random_state=42)

# Measure the training time for serial processing
start_time = time.time()
rf_serial.fit(X_train, y_train)
serial_duration = time.time() - start_time

# Predict and calculate accuracy
y_pred_serial = rf_serial.predict(X_test)
accuracy_serial = accuracy_score(y_test, y_pred_serial)

# Output the results for serial processing
print(f"Serial training time: {serial_duration:.4f} seconds")
print(f"Serial accuracy: {accuracy_serial:.4f}")
```
