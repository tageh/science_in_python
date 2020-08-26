import matplotlib.pyplot as plt
import numpy as np

#Data to be plotted

x = ['Alfa', 'Beta', 'Gamma']
y = np.array([10,20,30])

#Poltting

plt.close('all')
plt.figure(1, figsize =(12,9))

plt.bar(x,y, width=0.9, color=('green','blue','red'))

#Plots text on top of each bar using plt.txt()

offset_y = 0.5

for k in range(0, len(x)):
    plt.text(x[k], y[k]+offset_y, str(y[k]))

plt.title("Gjeldsoversikt")
plt.xlabel("Bankens navn")
plt.ylabel("Gjeld [MNOK]")

plt.show()

