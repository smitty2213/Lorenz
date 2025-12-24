import matplotlib.pyplot as plt
import csv
import uuid
from itertools import zip_longest
'''
Lorenz Equations
dx/dt = sigma(y-x)
dy/dt = x(p-z) - y
dz/dt = xy-Bz

B,p,sigma are paramaeters
'''

def lorenz(x,y,z, sigma, p, B):
    dxdt = sigma*(y-x)
    dydt = x*(p-z)-y
    dzdt = x*y-B*z
    return dxdt, dydt, dzdt

pos_dwell_time=[]
neg_dwell_time=[]

#Arrays to store values to be plotted and traced in the data file
x_array = []
y_array = []
z_array = []
t_array = []

#Inital conditions
x,y,z = 2,5,6
dt = .01
sigma, p, B = 10, 28, 8/3
t = 0.0
steps = 10000

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

#Create a unique file name
run_id = uuid.uuid4().hex[:8]
filename = f"data_run_{run_id}.csv"

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(["Positive Dwell Time", "Negative Dwell Time"])

    for positive_time, negative_time in zip_longest(pos_dwell_time, neg_dwell_time, fillvalue=''):
        writer.writerow([positive_time, negative_time])



plt.plot(x_array, z_array)
plt.xlabel("X")
plt.ylabel("Z")
plt.show()







