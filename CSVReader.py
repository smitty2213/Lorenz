import matplotlib.pyplot as plt
import pandas as pd

file = "data_run_e81c7f78.csv"
dataframe = pd.read_csv(file)
x = dataframe["Changing Variable"]
neg_dwell_time = dataframe["mean_neg_dwell_time"]
pos_dwell_time = dataframe["mean_pos_dwell_time"]



plt.plot(x, neg_dwell_time)
plt.plot(x, pos_dwell_time)
plt.xlabel("Changing Variable")
plt.ylabel("Average Dwell Times")
plt.legend(["Negative Dwell Time", "Positive Dwell Time"])
plt.show()



