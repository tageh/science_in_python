import numpy as np 

def sirkel(r):
    ar = np.pi*r**2
    om = 2*np.pi*r

    return ar, om

r = 5

areal,omkrets = sirkel(r)

print('Areal er:', areal, 'Omkrets er:',omkrets )

for x in range(1,11):
    areal,omkrets = sirkel(x)
    print('Areal for',x, 'er:',areal)


