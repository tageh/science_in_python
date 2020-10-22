import numpy as np  


n=10
sum = 0
for i in range(n):
    sum += 1/(i+1)

print(sum)


n = 0
sum = 0

while sum < 10:
    n+=1
    sum += 1/(n+1)
    
    
print('n må være', n, 'for at summen skal bli over 10.\nDen vil da være', sum )