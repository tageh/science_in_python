import numpy as np 

n = 10
summen = 0

for x in range(n):
    summen += 1/(x+1)

'''
teller = 0
summ = 0
while summ< 10:
    teller +=1
    summ += 1/(1+teller)

print(teller)

print(summen)'''

sum = 0
n = 1
while sum < 10:
    n+=1
    ledd = 1/n
    
    sum = sum + ledd

print('n skal være',n)