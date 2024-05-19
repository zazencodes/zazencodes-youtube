# Dask

Install

```bash
python3.12 -m venv venv
venv/bin/pip install 'dask[complete]'
```

Demo

```python
df = dd.read_csv("~/Downloads/Video_Games_Sales_as_at_22_Dec_2016.csv")
df.head()
df = dd.read_csv("~/Downloads/Video_Games_Sales_as_at_22_Dec_2016.csv", dtype={"User_Score": "object", "Year_of_Release": "float64"})
df.head()
df.groupby("Genre").value_counts()
task = df.groupby("Genre").value_counts()
type(task)
task.compute()
```

Create data for demo at scale

```python
import pandas as pd
import numpy as np

# Generate a large DataFrame with random data
num_rows = 10**8
data = {
    'id': np.random.randint(0, 1000, size=num_rows),
    'value': np.random.rand(num_rows),
    'timestamp': pd.date_range('2021-01-01', periods=num_rows, freq='s')
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('large_demo_data.1.csv', index=False)
```

```bash
cp large_demo_data.1.csv large_demo_data.2.csv
cp large_demo_data.1.csv large_demo_data.3.csv
cp large_demo_data.1.csv large_demo_data.4.csv
```

Open htop and two more panes

```python
# With pandas
df = pd.concat((pd.read_csv(f"large_demo_data.{i+1}.csv") for i in range(4)))

# With dask
df = dd.read_csv("large_demo_data.*.csv"); print(len(df))
df.columns
df.head()
df.id[:1e5].value_counts().compute()
```


