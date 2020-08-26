import matplotlib.pyplot as plt
import numpy as np

data = np.array([1,2,3,4,5,6])
data_norm = data/sum(data)
my_labels = ['Pi: ' + str(data[0]),
            'Upsilon: ' + str(data[1]),
            'Theta: ' + str(data[2]),
            'Eta: ' + str(data[3]),
            'Omikron: ' + str(data[4]),
            'Nu: ' + str(data[5])]

plt.close('all')
plt.figure(1, figsize = (12,9))

plt.rc('font', size=12)
plt.pie(data_norm, labels=my_labels, autopct = '%.1f%%')
plt.title('Figure title')

plt.show()
