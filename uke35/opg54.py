import numpy as np

def storeKatet(lk,hy):
    sk = np.sqrt((hy**2)-(lk**2))

    return sk

lk = float(input("Skriv inn lengden på lille katet: "))
hy = float(input("Skriv inn lengden på hypotenusen: "))

print(storeKatet(lk,hy))
