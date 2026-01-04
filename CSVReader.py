import matplotlib.pyplot as plt
import pandas as pd

file = "data_run_077fc3e0.csv"
dataframe = pd.read_csv(file)
y = dataframe.groupby("Changing Variable")
neg_mean_dwell_time = y["mean_neg_dwell_time"].mean()
pos_mean_dwell_time = y["mean_pos_dwell_time"].mean()
x = neg_mean_dwell_time.index

neg_std = y["mean_neg_dwell_time"].std()
pos_std = y["mean_pos_dwell_time"].std()


plt.errorbar(x, neg_mean_dwell_time, yerr=neg_std, fmt=".")
plt.errorbar(x, pos_mean_dwell_time, yerr=pos_std, fmt=".")
plt.xlabel("Changing Variable")
plt.ylabel("Mean Dwell Time")
plt.legend(["Negative Dwell Time", "Positive Dwell Time"])
plt.show()













