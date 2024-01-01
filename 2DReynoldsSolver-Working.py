import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm


#independent variables
nx, nz = 100, 100
xmax, zmax = 1, 1
dx = xmax/nx
dz = zmax/nz
z = np.linspace(0, zmax, nz)
x = np.linspace(0, xmax, nx)


#constants and initial conds
mu = 10**(-3) #Pa s
U = 20 #m/s
    
#film thickness and stuff
slope = -0.04*10**(-3)
yint = 0.02*10**(-3)
h = np.zeros([nx, nz])
for xcount in range(1, nx - 1):
    for zcount in range(1, nz - 1):
        h[xcount, zcount] = slope*xcount + yint
#h[1:nx-1, 1] = slope*x + yint

#iterations to do
n = 1000

def dhdx():
    return slope

def dhdz():
    return slope

def solve(it):
    A, B, C, D, E = np.zeros([nx, nz]), np.zeros([nx, nz]), np.zeros([nx, nz]), np.zeros([nx, nz]), np.zeros([nx, nz])
    #solution variables
    p_old = np.zeros([nx, nz])
    p_new = np.zeros([nx, nz])
    for out in range(it):
        A[1:nx -1, 1:nz - 1] = ((1/(dx**2)) - (3/(2*dx*h[1:nx -1, 1:nz -1]))*dhdx())/(
            2*((1/dx**2) + (1/dz**2)))        
        B[1:nx -1, 1:nz - 1] = ((1/(dz**2)) - (3/(2*dz*h[1:nx -1, 1:nz -1]))*dhdz())/(
            2*((1/dx**2) + (1/dz**2))) 
        C[1:nx -1, 1:nz - 1] = ((1/(dx**2)) + (3/(2*dx*h[1:nx -1, 1:nz -1]))*dhdx())/(
            2*((1/dx**2) + (1/dz**2))) 
        D[1:nx -1, 1:nz - 1] = ((1/(dz**2)) + (3/(2*dz*h[1:nx -1, 1:nz -1]))*dhdz())/(
            2*((1/dx**2) + (1/dz**2))) 
        E[1:nx -1, 1:nz - 1] = ((-3*mu*U)/((h[1:nx -1, 1:nz -1]**3)*((1/dx**2) + (1/dz**2))))*dhdx()
        
        p_new[1:nx - 1, 1:nz - 1] = (A[1:nx - 1, 1:nz - 1]*p_old[0:nx - 2, 1:nz - 1] + 
                                     B[1:nx - 1, 1:nz - 1]*p_old[1:nx - 1, 0:nz - 2] + 
                                     C[1:nx - 1, 1:nz - 1]*p_old[2:nx, 1:nz - 1] + 
                                     D[1:nx - 1, 1:nz - 1]*p_old[1:nx - 1, 2:nz] + 
                                     E[1:nx - 1, 1:nz - 1])
        p_old = p_new
    
    return p_new

def display():
    pass

def main():
    soln = solve(n)
    fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})

    a, b = np.meshgrid(x, z)
    surf = ax.plot_surface(a, b, soln, cmap = cm.viridis, linewidth = 0, antialiased = False)
    
    
if __name__ == '__main__':
    main()
    