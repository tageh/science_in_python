import numpy as np
import matplotlib.pyplot as plt 

x = np.array([0,1,2,3,4,5])
y = x
z = np.sqrt(y)

plt.figure(1, figsize=(12,9))

plt.subplot(2,1,1)
plt.plot(x,y,'r*-' , color='red')
plt.xlabel('x [s]')
plt.ylabel('[m]')
plt.legend(('y'))
plt.grid()

plt.subplot(2,1,2)
plt.plot(x,z, 'bo-' ,color='blue')
plt.xlabel('x [s]')
plt.ylabel('[m]')
plt.legend(('z'))
plt.grid()

plt.show()

plt.savefig('plott2.pdf')