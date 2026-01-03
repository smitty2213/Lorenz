import matplotlib.pyplot as plt
import pandas as pd

file = "data_run_7f3d8e41.csv"
dataframe = pd.read_csv(file)
x = dataframe["Changing Variable"]
neg_dwell_time = dataframe["mean_neg_dwell_time"]
pos_dwell_time = dataframe["mean_pos_dwell_time"]

neg_time_fraction = dataframe["neg_time_fraction"]
pos_time_fraction = dataframe["pos_time_fraction"]



plt.plot(x, neg_dwell_time)
plt.plot(x, pos_dwell_time)
plt.xlabel("Changing Variable")
plt.ylabel("Average Dwell Times")
plt.legend(["Negative Dwell Time", "Positive Dwell Time"])
plt.show()

plt.plot(x, neg_time_fraction)
plt.plot(x, pos_time_fraction)
plt.xlabel("Changing Variable")
plt.ylabel("Occupancy Fraction")
plt.legend(["Negative Occupancy", "Positive Occupancy"])
plt.show()






