import numpy as np 
import matplotlib.pyplot as plt     

def f(x):
    return 2*np.sin(x)+ 5/2

x = np.linspace(1,20,1000)

y = np.array(f(x))

lengde = len(y)

for index in range(0, lengde):
    if y[index] > 4:
        y[index] = 4
    if y[index] < 1:
        y[index] = 1

plt.figure()
plt.plot(x,y, linewidth=3)
plt.show()