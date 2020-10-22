import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return 2*np.sin(x)+5/2

x = np.linspace(1,20,1000)

y = np.array(f(x))
lende = len(y)


for i in range(0,lende):
    if y[i] > 4:
        y[i] = 4
    if y[i] < 1:
        y[i] = 1

    
plt.figure()
plt.plot(x,y)
plt.show()