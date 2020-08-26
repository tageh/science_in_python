import numpy as np
import matplotlib.pyplot as plt 

x = np.array([0,1,2,3,4,5])
y = x
z = np.sqrt(y)

plt.figure(1, figsize=(12,9))

plt.plot(x,y,'r*-' , color='red')
plt.plot(x,z, 'bo-' ,color='blue')
plt.xlabel('x [s]')
plt.ylabel('[m]')
plt.grid()
plt.legend(('y',"z"))
plt.show()

plt.savefig('plott1.pdf')