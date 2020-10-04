import numpy as np 

n = 100000
r=1
inside = 0

for k in range(0,n):
    [x_coor, y_coor] = np.random.random(2)
    dist = np.sqrt(x_coor**2 + y_coor**2)

    if(dist<r):
        inside +=1

print(4*inside/n)