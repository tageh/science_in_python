import numpy as np 
import matplotlib.pyplot as plt


fil = np.loadtxt("klima.txt", delimiter=" ")

aarstall = fil[:, 0]
midtemp = fil[:, 1]

maks = np.argmax(midtemp)
ymaks = aarstall[maks]

minn = np.argmin(midtemp)
ymin = aarstall[minn]


print("makstemp:", midtemp[maks], "i år", ymaks)

print("makstemp:", midtemp[minn], "i år", ymin)

mid_temp = np.mean(midtemp[61:90])
mid = mid_temp*np.ones(len(midtemp))

print("midtemp er", mid_temp)
plt.plot(aarstall, midtemp, 'r*', aarstall, mid)
plt.show()

