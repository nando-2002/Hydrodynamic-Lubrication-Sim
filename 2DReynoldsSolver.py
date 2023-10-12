import numpy as np 
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator
#init space
nx = 100
nz = 100

xmax = 1
zmax = 1

x = np.linspace(0, xmax, nx)
z = np.linspace(0, zmax, nz)
dx = xmax/nx
dz = zmax/nz

p_old = np.zeros([nx, nz])
p_new = np.zeros([nx, nz])

#init of film thickness values and derivatives

A = -0.04*10**(-3)
B = 0.02*10**(-3)

def h(i):
    return (A*i + B)

def dhdx(i):
    return A

def dhdz(i):
    return 0

def dh3dx(i):
    return 3*A*h(i)

def dh3dz(i):
    return 0

#init of fluid values and boundary conditions

mu = 10**(-3)#Pa s
U = 20#m/s

for a in range(1000):
    for u in range(1, nx - 1):
        for v in range(1, nz - 1):
            p_new[u,v] = (1/((-2/(6*mu*U))*((dh3dx(u)/dx) + (dh3dz(v)/dz)))*(dhdx(u) - (1/(6*mu*u))*((dh3dx(u)*(p_old[u+1,v]+p_old[u-1,v]))+(dh3dz(v)*(p_old[u,v+1]+p_old[u,v-1])))))
    p_old = p_new
    
fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})

x, z = np.meshgrid(x, z)
surf = ax.plot_surface(x, z, p_new, cmap = cm.coolwarm, linewidth = 0, antialiased = False)