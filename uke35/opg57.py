import numpy as np

def kinetiskEnergi(m, v):
    ek = .5*m*v**2

    return ek

m = 80
v=12

print('Den kinetiske energien er: ',kinetiskEnergi(m,v), 'J')