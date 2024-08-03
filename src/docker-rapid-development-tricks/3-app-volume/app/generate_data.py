import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(0)
data = {
    "x1": np.random.rand(100),
    "x2": 2 * np.random.rand(100),
    "y": 3 * np.random.rand(100),
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("/data/input_data.csv", index=False)
