import numpy as np


l = np.linspace(-1,1)
tall = np.random.choice(l,3)

index = 0
teller = 0
y = 100000

while(index<y):
    a = np.random.choice(l,1)
    b = np.random.choice(l,1)
    c = np.random.choice(l,1)

    if a > 0 and b > 0 and c >0:
        teller+=1
    index +=1

x = teller/index

print("Sannsynlighet er: ", x)
with open('TrePositive.txt', 'w') as f:
    f.write("Sannsynligheten er: ")
    f.write(str(x))