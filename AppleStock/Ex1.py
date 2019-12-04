from matplotlib import pylab as plt
import pandas as pd

df = pd.read_excel("")
print(df)

df["Date"] = pd.to_datetime(df.date)
indexes = []
for date2 in df.Date:
