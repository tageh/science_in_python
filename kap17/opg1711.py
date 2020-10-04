import numpy as np 

n = 100000
teller = 0

sample_space = np.linspace(1,100,100)

for x in range(0,n):
    lodd = np.random.choice(sample_space, 2, False)

    if(np.abs(lodd[0] -lodd[1])==1):
        teller +=1

print(teller/n)