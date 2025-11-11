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
x,y,z = 7,6,3
dt = .01
sigma, p, B = 10, -10, 8/3

for n in range(0,10000):
    x_array.append(x)
    z_array.append(z)
    y_array.append(y)

    dxdt, dydt, dzdt = lorenz(x,y,z, sigma, p, B)
    x = x + dxdt*dt
    y = y + dydt*dt
    z = z + dzdt* dt

plt.plot(x_array,z_array)
plt.show()









