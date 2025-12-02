import matplotlib.pyplot as plt
import pandas as pd


x = pd.read_csv("data_run_fd97cb9f.csv", usecols=["t"])
y_pos = pd.read_csv("data_run_fd97cb9f.csv", usecols=["pos_flag"])
y_neg = pd.read_csv("data_run_fd97cb9f.csv", usecols=["neg_flag"])
y_neg = y_neg * -1

y_xValues = pd.read_csv("data_run_fd97cb9f.csv", usecols=["x"])


plt.plot(x,y_xValues)
plt.xlabel("Time")
plt.ylabel("Values of X")
plt.show()

plt.plot(x, y_neg)
plt.plot(x, y_pos)
plt.xlabel("Time")
plt.ylabel("Positive and Negative X")
plt.show()

