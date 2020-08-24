import numpy as np

def storstElement(array):
    leng = len(array)
    ant = np.amax(array)
    return ant, leng

a = np.array([1.2,5.9,-3.1,7.9,0.6])

(maks, antall) = storstElement(a)


print('Det er ', antall, 'elemeter og det største elemeter er ',maks)