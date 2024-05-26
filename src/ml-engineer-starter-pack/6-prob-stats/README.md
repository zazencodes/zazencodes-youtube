# Probability and stats

## Basic probability

- Use cases:
    - Foundational

```python
P_critical_hit = 0.05 # Probability of rolling a 20 on a D20

# Calculate the probability of rolling consecutive 20s on a D20
P_consecutive_critical_hits = {
    2: P_critical_hit * P_critical_hit,
    3: P_critical_hit * P_critical_hit * P_critical_hit,
    4: P_critical_hit * P_critical_hit * P_critical_hit * P_critical_hit,
}

```


## Conditional probabilities and Bayes theorem

- Use cases:
    - Baseline modeling, e.g. Naive Bayes

```python
P_D = 0.01  # Probability of having the disease
P_not_D = 1 - P_D  # Probability of not having the disease
P_T_given_D = 0.99  # Probability of a positive test given that the person has the disease
P_T_given_not_D = 0.05  # Probability of a positive test given that the person does not have the disease

# Calculate P(T), the total probability of a positive test
P_T = P_T_given_D * P_D + P_T_given_not_D * P_not_D

# Calculate P(D|T), the probability of having the disease given a positive test
P_D_given_T = (P_T_given_D * P_D) / P_T

# Print the result
print(f"The probability of having the disease given a positive test is {P_D_given_T:.4f}")
```




## Standard deviation

- Use cases:
    - Statistical testing, e.g. K-fold validation

```python
import numpy as np

# Sample dataset
data = [10, 12, 15, 18, 20]

# Calculate mean
mean = sum(data) / len(data)

# Calculate variance
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Calculate standard deviation using pure Python
std_deviation_python = np.sqrt(variance)

# Calculate standard deviation using NumPy
std_deviation_numpy = np.std(data)

print("Standard deviation using pure Python:", std_deviation_python)
print("Standard deviation using NumPy:", std_deviation_numpy)
```




## Correlation coefficient

- Use cases:
    - Feature selection
    - Multicollinearity detection

```python
import numpy as np

# Sample datasets
x = [1, 2, 3, 4, 5]
y = [-2, -4, -6, -8, -20]

# Calculate means
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Calculate variances
variance_x = sum((xi - mean_x) ** 2 for xi in x) / len(x)
variance_y = sum((yi - mean_y) ** 2 for yi in y) / len(y)

# Calculate standard deviations
std_deviation_x = np.sqrt(variance_x)
std_deviation_y = np.sqrt(variance_y)

# Calculate covariance
covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / len(x)

# Calculate Pearson correlation coefficient using pure Python
pearson_corr_python = covariance / (std_deviation_x * std_deviation_y)

# Calculate Pearson correlation coefficient using NumPy
pearson_corr_numpy = np.corrcoef(x, y)[0, 1]

print("Pearson correlation coefficient using pure Python:", pearson_corr_python)
print("Pearson correlation coefficient using NumPy:", pearson_corr_numpy)
```






## Normal distribution

- Use cases:
    - Modeling assumptions, e.g. linear regression assumes that residuals are normal
    - Feature engineering, e.g. normalization

```python
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Manual implementation of normal distribution
def norm_hand_coded(x, mean, std_dev):
    return (1/(std_dev*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mean)/std_dev)**2)

# Parameters for the distribution
mean = 0
std_dev = 1

# Generate x values
x_values = np.linspace(-5, 5, 1000)

# Calculate y values using manual function
manual_y_values = norm_hand_coded(x_values, mean, std_dev)

# Calculate y values using scipy's normal distribution function
scipy_y_values = norm.pdf(x_values, mean, std_dev)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, manual_y_values, label='Manual Normal Distribution', lw=10)
plt.plot(x_values, scipy_y_values, label='NumPy Normal Distribution', lw=3)
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
```









