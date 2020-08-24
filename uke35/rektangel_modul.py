import numpy as np

def arealRektangel(l,b):
    return l*b

def omkretsRektangel(l,b):
    return 2*(l+b)

def diagonalRektangel(l,b):
    dig = np.sqrt((l**2)+(b**2))
    return dig