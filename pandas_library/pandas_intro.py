import pandas as pd
import numpy as np

# pandas = package for data analysis, time series and statistics (YOU CAN USE DATES!!!)
# numpy = package for arrays

s = pd.Series([1, 3, 5, np.nan])
# print(s)

dates = pd.date_range("20191101", periods=7)
# print(dates)

# np.random.randn(n1, n2) n1 = row, n2 = column (GENERATES AN ARRAY OF RANDOM NUMBERS)

df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list("ABCD"))
print(df)
print("")

# describe gives you: info about the column = "series" (count, mean, std, min, 25%, 50%, 75%, max)
print(df.describe())

print("")

# select by label: loc
print(df.loc [ [dates[2], dates[3], dates[3]], ["B", "C"] ] )


