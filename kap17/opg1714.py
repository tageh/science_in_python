import numpy as np

n = 100000
teller = 0

#kode = np.random.choice(sample_space)

sample_space = np.linspace(100,999,900)
sample_size = 50
replace = False

kode = np.random.choice(sample_space)

for x in range(0,n):
    test = np.random.choice(sample_space,sample_size,replace)

    for t in test:
        if(t == kode):
            teller = teller + 1
            break

print(teller/n)