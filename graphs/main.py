from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

f1 = pd.read_csv("bmw.csv")
f1["Date"] = pd.to_datetime(f1.Date)

f2 = pd.read_csv("ferrari.csv")
f2["Date"] = pd.to_datetime(f2.Date)

f3 = pd.read_csv("toyota.csv")
f3["Date"] = pd.to_datetime(f3.Date)

""""
f4 = pd.read_excel("data points.xlsx")
f4["Dates"] = pd.to_datetime(f4["Dates"], format("%Y"))
indexes = []

for data_point in f4["Dates"]:
    indexes.append(data_point)
    
   
indexes2 = []
indexes3 = []
print(indexes1)
print(f4["Dates"])

for data_points in f4["Dates"]:
    for index, date in enumerate(f1.Date):
        if data_points == date:
            indexes1.append(index)

for data_points in f4["Dates"]:
    for index, date in enumerate(f2.Date):
        if data_points == date:
            indexes2.append(index)

for data_points in f4["Dates"]:
    for index, date in enumerate(f3.Date):
        if data_points == date:
            indexes3.append(index)
"""

# I tried to plot it with markers for the last year but i could not make it.
plt.figure("Stocks")
plt.plot(f1["Date"], f1["Close"], "r-", linewidth=0.5, label="BMW stock")
plt.plot(f2["Date"], f2["Close"], "b-", linewidth=0.5, label="FORD stock")
plt.plot(f3["Date"], f3["Close"], "g-", linewidth=0.5, label="TOYOTA stock")
plt.xlabel("Dates")
plt.ylabel("Stock Price")
plt.legend(loc="upper left")

print("SHOWING ON PANDAS' GRAPH BRO")
plt.show()
