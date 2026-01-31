import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file = "data_run_6143af4a.csv" #Big picture overview data
file2 = "run_level_data_ff8645fa.csv" #Run level data

#Dataframes to hold the data
#dataframe = pd.read_csv(file)
dataframe2 = pd.read_csv(file2)

#Variables
deltaT = 0.1 #Bin Width [0, detlaT), [deltaT, 2 * deltaT), ...
cols = ["Pos Dwell Time", "Neg Dwell"]
dataframe2[cols] = dataframe2[cols].apply(pd.to_numeric, errors = "coerce") #Turns any empty spaces from String to numbers and replace the dataframe with numberics
maxT = dataframe2[cols].to_numpy() #Crate a numpy array
maxT = np.nanmax(maxT) #Max value ignoring the blank space that would have this read as NaN


#Setup bin edges
bins = np.arange(0, maxT + deltaT, deltaT)

#Turn the two columns into one array
posdwell = dataframe2["Pos Dwell Time"]
negdwell = dataframe2["Neg Dwell"]
totaldwell = pd.concat([posdwell, negdwell], ignore_index=True).dropna() #Stackes the two columns and restes the indexing 

#Histogram for dwell time probabilities
data = totaldwell.to_numpy() #Convert the totaldwell dataframe to a numpy arraye
lam = 1/np.mean(data) #For plotting an exponential curve on the graph
t = np.linspace(0, maxT, 10000)
pdf = lam * np.exp(-lam * t)

plt.hist(data, bins=bins, density=True)
plt.plot(t, pdf)
plt.xlabel("Dwell Time")
plt.ylabel("Density")
plt.show()

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


















