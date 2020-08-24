import numpy as np

def potensiellEnergi(ep, m,g=9.81):
    #g = 9.81
    h = ep/(m*g)
    return h

ep = 34.37
m = 0.48

print('høyden er: ',round(potensiellEnergi(ep,m),3))