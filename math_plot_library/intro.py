from matplotlib import pylab as plt

series1 = []
series2 = []
series3 = []

for i in range(0,30):
    series1.append(i)
    series2 += [i*i]
    series3 += [i**3]

# if you would like to plot it in different windows, with a single graph use the built in function called
# figure

# if you want to visualize them together just delete the "figure" code

plt.figure("first")
plt.plot(list(range(0, 30)), series1, "r+", label="Linear", linewidth=2, ms=10)
plt.plot(list(range(0, 30)), series2, "k^:", label="Quadratic", linewidth=0.5)
plt.legend(loc="upper left")
plt.figure("third")
plt.plot(list(range(0, 30)), series3)

# The FIRST ".figure" creates the graph, the SECOND ".figure" selects the graph
# You can add other built-in functions: "title", "ylim / xlim" (limits), "xlabel / ylabel" (labels)

plt.figure("first")
plt.ylim(0, 1000)
plt.xlabel("Series")
plt.ylabel("Linear Progression")
plt.title("Linear & Quadratic")

plt.figure("third")
plt.title("Cubic")
plt.ylim(0, 1000)
plt.ylabel("Cubic Progression")

plt.show()

# For more info please visit: "www.matplotlib.org"
