import numpy as np 

sample_space = np.array([1,2,3,4,5,6])
sample_size = 2
replace = True
prob = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

n=100000
teller = 0

for x in range(0,n):
    kast = np.random.choice(sample_space, sample_size,replace, prob)

    if(kast[0] == kast[1]):
        teller += 1


print('Sannsynlighet for å få to like:',teller/n)