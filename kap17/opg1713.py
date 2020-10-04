import numpy as np 

n = 100000
teller = 0

sampel_space = ['D','D','D','D','D','V','V','V','V','V','V','V','V','V','V']
sampel_size = 5
replace = False

for x in range(0,n):
    trekk = np.random.choice(sampel_space,sampel_size,replace)
    trekk.sort()
    if(trekk[-3] == 'V'):
        teller +=1

print(teller/n)