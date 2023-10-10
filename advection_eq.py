import numpy as np
import matplotlib.pyplot as plt
# import time

def visualize(xtitle, ytitle, var, ylimup, colour):
    plt.style.use("classic")
    plt.plot(np.linspace(0,xmax,nx), var, colour)   
    plt.ylim(-0.01,ylimup) 
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.grid()
    plt.show()

#initializing values
nx = 1000
nt = 2500 #1500
xmax = 2*np.pi
dx = xmax/(nx - 1)
v = 1
dt = 0.0025

eps = v*dt/dx #staility criterion
print("Stability Criterion: ", round(eps, 3))

u = np.zeros(nx)
u_past = np.zeros(nx)

sig = 30 #increases the width of the initial distribution
wavepos = 100 #determines the initial x position of the wave
#initial wave condition - gaussian function 
for i in range(nx):
    u_past[i] = np.exp(-(i - wavepos)**2/sig**2)
    
visualize("space","magnitude (arbitrary quantity)", u_past, 2, "b-")

for a in range(nt):
    for j in range(1, nx-1):
        u[j] = -(0.5*v*dt/dx)*(u_past[j+1] - u_past[j - 1]) + u_past[j]
    # visualize("space","magnitude (arbitrary quantity)", u, 2, "r-")
    u_past = u
    j = 0
    
visualize("space","magnitude (arbitrary quantity)", u, 2, "r-")
    