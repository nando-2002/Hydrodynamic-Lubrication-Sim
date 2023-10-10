import numpy as np
import matplotlib.pyplot as plt

plt.clf()
#init of space

nx = 100
xmax = 1
x = np.linspace(0, xmax, nx)
dx = xmax/nx

#init of dependent

p_old = np.zeros(nx)
p_new = np.zeros(nx)

#init of film thickness values

A = -0.04*10**(-3)
B = 0.02*10**(-3)


def h(i):
    return (A*i + B)
"""
def dhdx(i):
    return (A)

def dh3dx(i):
    return (3*A*(h(i)))
"""
#visualization func

def visualize(xtitle, ytitle, var, colour):
    plt.style.use("classic")
    plt.plot(np.linspace(0,xmax,nx), var, colour)   
    #plt.ylim(-0.01,ylimup) 
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.grid()
    plt.show()
    

#init of BCs and consts

mu = 10**(-3) #Pa s
U = 20 #m/s

#solution 
for b in range(2000):
    for j in range(1, nx - 1):
        p_new[j] = (-mu*U*(dx**2)/(h(j))) + (p_old[j-1] + p_old[j+1])/2
    p_old = p_new
    
    if (b%100 == 0):
        if (b > 1800):
            visualize("Position along the bearing", "Pressure", p_new, "r-")
        else:
            visualize("Position along the bearing", "Pressure", p_new, "b-")  
    
