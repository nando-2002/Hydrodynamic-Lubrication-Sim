import numpy as np 
import matplotlib.pyplot as plt
from sympy import *

from matplotlib import cm

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

M = -0.04*10**(-3)
N = 0.02*10**(-3)
O = 0.01*10**(-3)
def h(i, j):
    i, j = symbols('i j')
    f = (M*i + N + O*(j + (nz*dz/2))**2)
    ff = f.subs([(i,i),(j,j)])
    return f

def dhdx(i, j):
    i, j = symbols('i j')
    f = (M*i + N + O*(j + (nz*dz/2))**2)
    ff = f.subs([(i,i),(j,j)])
    return diff(ff, i)

def dhdz(i, j):
    i, j = symbols('i j')
    f = (M*i + N + O*(j + (nz*dz/2))**2)
    ff = f.subs([(i,i),(j,j)])
    return diff(ff, j)

def dh3dx(i, j):
    i, j = symbols('i j')
    f = (M*i + N + O*(j + (nz*dz/2))**2)
    ff = f.subs([(i,i),(j,j)])
    return diff(ff**3, i)

def dh3dz(i, j):
    i, j = symbols('i j')
    f = (M*i + N + O*(j + (nz*dz/2))**2)
    ff = f.subs([(i,i),(j,j)])
    return diff(ff**3, j)

#init of fluid values and boundary conditions

mu = 10**(-3)#Pa s
U = 20#m/s

for a in range(500):
    for u in range(1, nx - 1):
        for v in range(1, nz - 1):
            #print(u, v, a)
            A = 6*mu*U*dx
            B = 6*mu*U*dz
            p_new[u,v] = ( (1/(-2*((dh3dx(u, v)/A) + (dh3dz(u, v)/B)))) 
                *(dhdx(u, v) - (dh3dx(u, v)/A)*(p_old[u + 1, v] + p_old[u - 1, v])
                          - (dh3dz(u, v)/B)*(p_old[u, v + 1] + p_old[u, v - 1])
                    )
                )
    p_old = p_new
    
fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})

x, z = np.meshgrid(x, z)
surf = ax.plot_surface(x, z, p_new, cmap = cm.viridis, linewidth = 0, antialiased = False)