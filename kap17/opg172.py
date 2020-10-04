import numpy as np 
import matplotlib.pyplot as plt 

hoyde = np.array([600, 470, 170, 430, 300])

middelverdi = sum(hoyde)/len(hoyde)
standaravik = np.sqrt(np.sum((hoyde - middelverdi)**2) / (len(hoyde)-1))

x = range(1,400)

print('middelverdi:', middelverdi,'\nstandardavik:',standaravik)

plt.plot(hoyde, 'r*')
plt.plot([middelverdi, middelverdi,middelverdi,middelverdi,middelverdi,middelverdi])
plt.plot([standaravik, standaravik,standaravik,standaravik,standaravik,standaravik])
plt.show()

#litt fail men ahah
