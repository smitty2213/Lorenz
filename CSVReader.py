import matplotlib.pyplot as plt
import pandas as pd

file = "data_run_6143af4a.csv"
file2 = "run_level_data_8133c33b.csv"

#Dataframes for each graph
dataframe = pd.read_csv(file)
run_level_dataframe = pd.read_csv(file2)

#Mean Dwell Time Graph, commenting this out until needed
'''y = dataframe.groupby("Changing Variable")
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
plt.show()'''

#Histogram for dwell time probabilities















