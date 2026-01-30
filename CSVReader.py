import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file = "data_run_6143af4a.csv" #Big picture overview data
file2 = "run_level_data_8133c33b.csv" #Run level data

#Dataframes to hold the data
#dataframe = pd.read_csv(file)
dataframe2 = pd.read_csv(file2)

#Variables
deltaT = 2 #Bin Width 
cols = ["Pos Dwell Time", "Neg Dwell"]
dataframe2[cols] = dataframe2[cols].apply(pd.to_numeric, errors = "coerce") #Turns any empty spaces from String to numbers and replace the dataframe with numberics
maxT = dataframe2[cols].to_numpy() #Crate a numpy array
maxT = np.nanmax(maxT) #Max value ignoring the blank space that would have this read as NaN



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
















