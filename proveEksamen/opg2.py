import numpy as np  
import matplotlib.pylab as plt
'''
def ReLu(x):
    if(x>0):
        return x
    else:
        return 0
'''
def ReLu(X):
   return np.maximum(0,X)

#print(relu(-32))


ax = np.linspace(-1,1,100)

plt.plot(ax, ReLu(ax))
plt.show()