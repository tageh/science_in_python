import numpy as np
import matplotlib.pyplot as plt 

n = 1000

sample_space = np.linspace(1,365,365)
antall = np.linspace(2,50,49)
prosent = np.zeros(49)

for x in range(2,51,1):
    teller = 0
    
    for i in range(0,n):
        bdag = np.random.choice(sample_space,50)
        bdag.sort()
        for i in range(0,len(bdag)-1,1):
            if(bdag[i] - bdag[i+1] == 0):
                teller +=1
                break
    prosent[x-2] = teller / n



plt.plot(antall, prosent)
plt.show()
