import numpy as np 

# mynt = 2 kron = 1

sample_space = np.array([1,2])

n = 100000
teller = 0

for x in range(0,n):
    kast = np.random.choice(sample_space,5)

    if(sum(kast) == 5):
        teller += 1

print(teller/n)