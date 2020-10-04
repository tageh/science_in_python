import numpy as np 

#mynt = 1 kron =2

sample_space = np.array([1, 2])

teller = 0
n = 10000

for x in range(0,n):
    kast = np.random.choice(sample_space,3)

    if(sum(kast) == 5 ):
        teller += 1
    

print(teller/n)