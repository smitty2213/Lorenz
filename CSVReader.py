import matplotlib.pyplot as plt
import pandas as pd

file = "data_run_06999c3a.csv"
x = pd.read_csv(file, usecols=["t"])
y_pos = pd.read_csv(file, usecols=["pos_flag"])
y_neg = pd.read_csv(file, usecols=["neg_flag"])
y_neg = y_neg * -1

y_xValues = pd.read_csv(file, usecols=["x"])


plt.plot(x,y_xValues)
plt.xlabel("Time")
plt.ylabel("Values of X")
plt.show()

plt.plot(x, y_neg)
plt.plot(x, y_pos)
plt.xlabel("Time")
plt.ylabel("Positive and Negative X")
plt.show()

