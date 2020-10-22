import numpy as np

n = 0
summ = 0

for i in range(10):
    n+=1
    summ += n/(n+1)

print(summ)


while summ < 100:
    n+=1
    summ += n/(n+1)

print(n)
print(summ)