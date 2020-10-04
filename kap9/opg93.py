import numpy as np 
import matplotlib.pyplot as plt 

def T(x):
    return 7-10*np.cos( ((2*np.pi)/365)*x - ((5*np.pi)/73))

ax = int(np.linspace(1,365,365))

plt.plot(ax, T(ax))
plt.show()

M = np.array([ax, T(ax)]).T

np.savetxt('tempratur.txt', M, fmt='%.3f', delimiter=" ")