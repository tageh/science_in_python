import numpy as np
import matplotlib.pyplot as plt 

M = np.loadtxt('ra_data.txt', delimiter=' ')

Kj = M[:, 0] #Kjønn
Kl = M[:, 1] #klassetrin
Timer = M[:, 2] #Antall timer

gutter = 0
jenter = 0

for n in range(0 , len(Kj), 1):
    if(Kj[n] == 1):
        gutter = gutter + 1
    else:
        jenter = jenter + 1

labels = ['Gutter', 'Jenter']
sizes = [gutter,jenter]

plt.close('all')
plt.figure(1, figsize=(12,9))
plt.pie(sizes, labels=labels ,autopct='%.1f%%')
plt.axis('equal')
plt.show()