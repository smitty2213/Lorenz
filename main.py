import csv
import uuid
from itertools import zip_longest
import os

'''
Lorenz Equations
dx/dt = sigma(y-x)
dy/dt = x(p-z) - y
dz/dt = xy-Bz

B,p,sigma are paramaeters

'''
#Lorenz Equations
def lorenz(x,y,z, sigma, p, B):
    dxdt = sigma*(y-x)
    dydt = x*(p-z)-y
    dzdt = x*y-B*z
    return dxdt, dydt, dzdt

#A function to sweep a designated variable for each of the chosen inital conditions below
'''def sweep():
    lorenz_value = []
    for n in range(0,1):
        for i in range(0,1):
            x0 = [1.0000001]
            y0 = [0]
            z0 = [0]
            lorenz_value.append(lorenz_run(n, x0[i], y0[i], z0[i]))
    return lorenz_value'''


def lorenz_run(varies, x0, y0, z0):
    pos_dwell_time=[]
    neg_dwell_time=[]

#Arrays to store values to be plotted and traced in the data file
    x_array = []
    y_array = []
    z_array = []
    t_array = []

#Inital conditions
    x,y,z = x0,y0,z0
    dt = .01
    sigma, p, B = 10, 28, 8/3
    t = 0.0
    steps = 100000000

    previous_crossing_time = t


    for n in range(steps+1):
        t_array.append(t)
        x_array.append(x)
        z_array.append(z)
        y_array.append(y)
        

        dxdt, dydt, dzdt = lorenz(x,y,z, sigma, p, B)
        xtrial = x + dxdt*dt
        ytrial = y + dydt*dt
        ztrial = z + dzdt* dt

        dxdt2, dydt2, dzdt2 = lorenz(xtrial,ytrial,ztrial, sigma, p, B)
    
        previous_x = x
    
        x= x + ((1/2)*(dxdt + dxdt2))*dt
        y= y + ((1/2)*(dydt + dydt2))*dt
        z= z + ((1/2)*(dzdt + dzdt2))*dt
    
        t += dt


        if previous_x < 0 and x > 0 :
            neg_dwell_time.append(t - previous_crossing_time)
            previous_crossing_time = t
        elif previous_x > 0 and x < 0:
            pos_dwell_time.append(t - previous_crossing_time)
            previous_crossing_time = t

    final_dwell = t - previous_crossing_time

    if x > 0:
        pos_dwell_time.append(final_dwell)
    elif x < 0:
        neg_dwell_time.append(final_dwell)

    mean_pos_dwell_time = sum(pos_dwell_time)/len(pos_dwell_time) if pos_dwell_time else 0.0
    mean_neg_dwell_time = sum(neg_dwell_time)/len(neg_dwell_time) if neg_dwell_time else 0.0

    pos_time_fraction = sum(pos_dwell_time)/t
    neg_time_fraction = sum(neg_dwell_time)/t

    total_time_fraction = pos_time_fraction + neg_time_fraction

    return (varies, mean_neg_dwell_time, mean_pos_dwell_time, pos_time_fraction, neg_time_fraction, 
    total_time_fraction, pos_dwell_time, neg_dwell_time, p, B, sigma, x0, y0, z0, steps, dt)

results = lorenz_run(varies=0, x0=1, y0=0, z0=0)

run_id = uuid.uuid4().hex[:8]
filename = f"data_event_run_{run_id}.csv"


with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Changing Variable", "mean_neg_dwell_time", "mean_pos_dwell_time", "pos_time_fraction", 
                     "neg_time_fraction","pos_fraction + neg_fraction", "p", "sigma", "B", "x0", "y0", "z0", "steps", "dt"])
    
    writer.writerow([results[0], results[1], results[2], results[3], results[4],results[5], results[8], results[10], 
                     results[9], results[11], results[12], results[13], results[14], results[15]])

filename2 = f"run_level_data_{run_id}.csv"

with open(filename2, 'w', newline='') as g:
    writer2 = csv.writer(g)
    writer2.writerow(["Pos Dwell Time", "Neg Dwell"])

    for pos_time, neg_time in zip_longest(results[6], results[7], fillvalue=""):
        writer2.writerow([pos_time, neg_time])












