import numpy as np 
import matplotlib.pyplot as plt 

def relu(x):
    return np.maximum(0,x)

print(relu(10))
print(relu(-1))

ax = np.linspace(-1,1, 100)

plt.plot(ax,relu(ax))
plt.show()