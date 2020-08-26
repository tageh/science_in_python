import numpy as np
import matplotlib.pyplot as plt

n = 10000
x = np.random.randn(n)
num_bins = 20

plt.figure(num=1, figsize=(24/2.54,18/2.54))

plt.hist(x,num_bins, color='green')
plt.grid()

plt.show()