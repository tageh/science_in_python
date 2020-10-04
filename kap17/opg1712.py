import numpy as np 

n = 100000
teller = 0

#rød = 1 grønn = 2 blå = 3
sample_space = np.array([2,2,2,1,1,3,3,3])

for x in range(0,n):
    trekk = np.random.choice(sample_space,3,False)

    if((1 in trekk) and (2 in trekk) and (3 not in trekk)):
        teller += 1

print(teller/n)