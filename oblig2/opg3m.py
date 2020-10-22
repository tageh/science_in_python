import numpy as np
import random

teller = 0
n = 100000
for i in range(n):
    t1 = random.uniform(-1,1)
    t2 = random.uniform(-1,1)
    t3 = random.uniform(-1,1)
    if t1 > 0 and t2 > 0 and t3 >0:
        teller += 1

san = teller/n

print('Sannsynlighet er:',san)

with open('Trepositive1.txt', 'w') as f:
    f.write("sansynligheten for 3 over 0 er: ")
    f.write(str(san))