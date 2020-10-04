import numpy as np  

fil = np.loadtxt('tempratur.txt', delimiter=' ')

dag = fil[: , 0]
temp = fil[: , 1]

tempMax = np.argmax(temp)
dagmax = dag[tempMax]

print("Maks temp var",temp[tempMax],"på dag",dagmax)

for i in range(1, len(temp), 1):
    if(temp[i]>10 and temp[i-1]<10):
        print("Dagen er", i)
    if(temp[i]<10 and temp[i-1]>10):
        print("Dagen er", i)