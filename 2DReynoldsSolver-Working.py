import numpy as np 
import matplotlib.pyplot as plt


#independent variables
nx, nz = 100
xmax, zmax = 1
dx = xmax/nx
dz = zmax/nz
z = np.linspace(0, zmax, nz)
x = np.linspace(0, xmax, nx)

#solution variables
p_old = np.zeros([nx, nz])
p_new = np.zeros([nx, nz])

#constants and initial conds
U = 2
mu = 2
    

def main():
    
if __name__ == '__main__':
    main()
    