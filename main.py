import matplotlib.pyplot as plt
import csv
import uuid
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

#Keep track of when x is positive and negative with a simple flag
pos_time_count = []
neg_time_count = []

#Arrays to store values to be plotted and traced in the data file
x_array = []
y_array = []
z_array = []
t_array = []

#Inital conditions
x,y,z = 3,5,6
dt = .01
sigma, p, B = 10, 28, 8/3
t = 0.0
steps = 10000

for n in range(steps+1):
    t_array.append(t)
    x_array.append(x)
    z_array.append(z)
    y_array.append(y)

    if x < 0 :
        pos_time_count.append(0)
        neg_time_count.append(1)
    if x > 0 :
        pos_time_count.append(1) 
        neg_time_count.append(0)
    if x == 0 :
        pos_time_count.append(0)
        neg_time_count.append(0)

    dxdt, dydt, dzdt = lorenz(x,y,z, sigma, p, B)
    xtrial = x + dxdt*dt
    ytrial = y + dydt*dt
    ztrial = z + dzdt* dt

    dxdt2, dydt2, dzdt2 = lorenz(xtrial,ytrial,ztrial, sigma, p, B)
    
    x= x + ((1/2)*(dxdt + dxdt2))*dt
    y= y + ((1/2)*(dydt + dydt2))*dt
    z= z + ((1/2)*(dzdt + dzdt2))*dt
    
    t += dt

#Time totals for positive and negative X values using the time count flags
pos_time_total = sum(pos_time_count)
neg_time_total = sum(neg_time_count)
total_time = pos_time_total + neg_time_total
pos_percent_time = (pos_time_total/total_time)*100
neg_percent_time = (neg_time_total/total_time)*100

#Create a unique file name
run_id = uuid.uuid4().hex[:8]
filename = f"data_run_{run_id}.csv"

with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["t", "x", "pos_flag", "neg_flag"])
    
    for ti, xi, posf, negf in zip(t_array, x_array, pos_time_count, neg_time_count):
        writer.writerow([ti, xi, posf, negf])
    
    writer.writerow(["Total positive time","Percent Positive", "Total negative time", "Percent Negative"])
    writer.writerow([pos_time_total,pos_percent_time, neg_time_total, neg_percent_time])


plt.plot(x_array, z_array)
plt.xlabel("X")
plt.ylabel("Z")
plt.show()







