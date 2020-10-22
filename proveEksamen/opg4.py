import numpy as np 

sample_space = np.array([1,2,3,4,5,6])
sample_size = 2
#replace = True
#prob = [1/6,1/6,1/6,1/6,1/6,1/6]

n = 100000
teller = 0
sekssum = 0
toer = 0

for x in range(0,n):
    kast = np.random.choice(sample_space,sample_size)

    if 6 in kast:
        teller+=1
    
    if kast[0] + kast[1] == 6:
        sekssum +=1
        if(kast[0] == 2 or kast[1] ==2):
            toer +=1



print('Sansynligheten for å få mist en sekser er:',teller/n)
print('Sansynligheten for å få en toer hvis summen er 6 er:',toer/sekssum)
'''

#Oppgave 4-2
import random
n = 100000    
en_sekser = 0
seks_som_sum = 0
en_toer = 0

for i in range(n):
    t1 = random.randint(1,6)
    t2 = random.randint(1,6)
    if t1 == 6 or t2 == 6:
        en_sekser += 1
    if t1 + t2 == 6:
        seks_som_sum += 1
        if (t1 == 2 or t2 == 2):
            en_toer += 1
    
print('Sansynligheten for å få minst en sekser er', en_sekser/n,
      '\nSansynligheten for å få en toer dersom summen er 6 er', en_toer/seks_som_sum)

'''   