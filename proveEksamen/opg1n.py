import numpy as np

def sirkel(r):
    areal = np.pi*r**2
    omkrets = 2*np.pi*r
    return areal,omkrets



#areal,omkrets = sirkel(r)

#print("areal er:", areal, "omkrets er:",omkrets)

for i in range(1,11):
    areal = sirkel(i)
    arr = np.array(areal)
    sa = sum(arr)
    print(arr, sa)