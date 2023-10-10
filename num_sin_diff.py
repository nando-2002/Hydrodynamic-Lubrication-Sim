import numpy as np
import math
import matplotlib.pyplot as plt

#Initializing values
xmax = 10*math.pi 
nx = 200 
dx = (xmax)/(nx - 1) 
x = np.linspace(0, xmax, nx)
k = 1 
#Calculating points per wavelength
npt = int(nx/(xmax/((2*math.pi)/k)))
f = np.sin(k*x) 
fa = k*np.cos(k*x)

plt.style.use("classic")
def output(b, m, n):
    plt.plot(x, b)
    #plt.title("Analytical")
    #plt.xlabel("x")
    #plt.ylabel("sin(x)")
    plt.xlim(1, xmax-1)
    plt.grid()
    
    plt.plot(x, m)
    plt.xlabel("x")
    plt.ylabel("d/dx sin(k*x)")
    plt.xlim(1, xmax-1)
    plt.grid()
    
    plt.plot(x, n)
    #plt.title("Analytical")
    #plt.xlabel("x")
    #plt.ylabel("sin(x)")
    plt.xlim(1, xmax-1)
    plt.grid()
    plt.show()
    
fc = np.zeros(nx)
error = 0
for i in range (1,nx -1):
    fc[i] = (f[i+1] - f[i-1])/(2*dx)
    error = ((fc[i] - fa[i])/(fa[i]))/2
plt.title("Numerical Central Difference")
output(fa, fc, (fa - fc))

plt.title("Analytical Derivative")
plt.plot(x, fa)
plt.title("Analytical")
plt.xlabel("x")
plt.ylabel("d/dx sin(k*x)")
plt.xlim(1, xmax-1)
plt.grid()

print(error)