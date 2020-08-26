import numpy as np
import matplotlib.pyplot as plt 

M = np.loadtxt('ra_data.txt', delimiter=' ')

Kj = M[:, 0] #Kjønn
Kl = M[:, 1] #klassetrin
Timer = M[:, 2] #Antall timer

t8 = 0
t9 = 0
t10 = 0

for n in range(0 , len(Timer), 1):
    if(Kl[n] == 8):
        t8 = t8 + Timer[n]
    elif(Kl[n] == 9):
        t9 = t9 + Timer[n]
    else:
        t10 = t10 + Timer[n]

klassetrinn = '8. Klasse', '9. Klasse', '10. Klasse'
sizes = [t8,t9,t10]


plt.close('all')
plt.figure(1, figsize=(12,9))
#plt.pie(sizes, labels=klassetrinn, autopct='%1.1f%%')
plt.bar(klassetrinn, sizes, width=0.5, color=('orange','blue','green'))

plt.show()



