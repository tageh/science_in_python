import numpy as np

def fart(arr, tid):
    t = len(arr)*tid
    summ = np.sum(arr)

    gjennomsnitt = summ/t

    return gjennomsnitt

t=2
S = np.array([1.05,1.30,1.10,0.94,1.21])

gs = fart(S,t)

print('Gjennomsnitt burde være: ', gs)