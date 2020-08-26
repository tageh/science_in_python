import numpy as np
import matplotlib.pyplot as plt 

M = np.loadtxt('ra_data.txt', delimiter=' ')

Kj = M[:, 0] #Kjønn
Kl = M[:, 1] #klassetrin
Timer = M[:, 2] #Antall timer

t8g = 0
t8j = 0
t9g = 0
t9j = 0
t10g = 0
t10j = 0

for n in range(0 , len(Kj), 1):
    if(Kl[n] == 8 and Kj[n] == 1):
        t8g = t8g + Timer[n]

    elif(Kl[n] == 8 and Kj[n] == 2):
        t8j = t8j + Timer[n]

    elif(Kl[n] == 9 and Kj[n] == 1):
        t9g = t9g + Timer[n]
    
    elif(Kl[n] == 9 and Kj[n] == 2):
        t9j = t9j + Timer[n]
    
    elif(Kl[n] == 10 and Kj[n] == 1):
        t10g = t10g + Timer[n]
    else:
        t10j = t10j + Timer[n]

labels = ['8 Klasse g', '8 klasse j', '9 klasse g', '9 klasse j', '10 klasse g', '10 klasse j']
sizes = [t8g, t8j, t9g, t9j, t10g, t10j]


plt.close('all')
plt.figure(1, figsize=(12,9))
#plt.pie(sizes, labels=klassetrinn, autopct='%1.1f%%')
plt.bar(labels, sizes)

plt.show()



