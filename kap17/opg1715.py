import numpy as np

n = 100000
teller = 0

sample_space = np.linspace(1,365,365)
sample_size = 23

for x in range(0,n):
    bdag = np.random.choice(sample_space,sample_size)
    bdag.sort()
    
    for i in range(0,len(bdag) -1 ,1):
        if(bdag[i] - bdag[i+1] == 0):
            teller +=1
            break


print(teller/n)
