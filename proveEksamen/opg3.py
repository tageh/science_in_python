import numpy as np  


n = int(input("Skriv et tall: "))
num = [i for i in np.arange(0,1,1/n)]

print(num)
print(sum(num))

'''
n = 0
while(True):
    n = n + 1
    num = np.arange(0,1,1/n)

    if(sum(num)<=10):
        print("Tall prøvd:",n)
    else:
        print("Tall funnet:",n)
        break
'''  
