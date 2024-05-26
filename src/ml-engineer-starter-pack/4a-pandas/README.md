# Pandas

Dataset: https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings

Load and explore data

```python
import pandas as pd
df = pd.read_csv("data/Video_Games_Sales_as_at_22_Dec_2016.csv.zip")
df.head()
df.tail()
df.dtypes
df.describe()
df.describe().T
df.isnull().sum()
df.NA_Sales.mean()
df.NA_Sales.median()
df.sort_values("NA_Sales", ascending=False).head()
df.groupby("Platform").Critic_Score.agg([len, np.mean]).sort_values("mean", ascending=False)
```


