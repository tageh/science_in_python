import numpy as np
import matplotlib.pyplot as plt

x1_array = np.array([0,1,2])
y1_array = x1_array * 10

x2_array = np.array([0,1,2])
y2_array = x2_array * (-10)


plt.figure(1)

plt.subplot(2,1,1)
plt.plot(x1_array, y1_array)
plt.xlabel("x1")
plt.ylabel("y1")
plt.grid()

plt.subplot(2,1,2)
plt.plot(x2_array, y2_array)
plt.xlabel("x2")
plt.ylabel("y2")
plt.grid()

plt.show()