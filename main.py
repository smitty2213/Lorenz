import matplotlib.pyplot as plt
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

x_array = []
y_array = []
z_array = []
x,y,z = 3,5,6
dt = 0.01
sigma, p, B = 10, 28, 8/3

for n in range(0,1000):
    x_array.append(x)
    z_array.append(z)
    y_array.append(y)

    dxdt, dydt, dzdt = lorenz(x,y,z, sigma, p, B)
    xtrial = x + dxdt*dt
    ytrial = y + dydt*dt
    ztrial = z + dzdt* dt

    dxdt2, dydt2, dzdt2 = lorenz(xtrial,ytrial,ztrial, sigma, p, B)
    
    x= x + ((1/2)*(dxdt + dxdt2))*dt
    y= y + ((1/2)*(dydt + dydt2))*dt
    z= z + ((1/2)*(dzdt + dzdt2))*dt

'''I want to investiage how long the path stays on one side of the z axis using the fact that the trajectroy hanges between
positive and negative x values'''

if x > 0

plt.plot(x_array, z_array)
plt.xlabel("X")
plt.ylabel("Z")
plt.show()







