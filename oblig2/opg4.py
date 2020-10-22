import numpy as np
import matplotlib.pyplot as plt 
import random

n = 10000
teller = 1
l0,l1,l2 = 0,0,0




for i in range(n):
    a = random.uniform(-5,5)
    b = random.uniform(-5,5)
    c = random.uniform(-5,5)  
    
    test =  b*b - 4*a*c

    if test>0:
        l2 +=1
    if test == 0:
        l1 +=1
    if test < 0:
        l0 +=1
    

data = np.array([l0,l1,l2])
#l0 = 0 løsning, l1 = 1 løsning og l2 = 2 løsninger
san = data/sum(data)

mlabels = ['0 løsninger: ' + str(l0),
          '1 løsning: ' + str(l1),
          '2 løsninger: ' + str(l2)
]

plt.figure(1)
plt.rc('font', size=10)
plt.pie(san, labels=mlabels,autopct='%.1f%%')
plt.show()

print(san)


