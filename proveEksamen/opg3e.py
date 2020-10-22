import numpy as np



for i in range(10):
    le = np.random.uniform(0,7.7)
    j = np.random.uniform(0,6)
    m = np.random.uniform(0,6)

    print(le,j,m)
    if le > j and j > m:
        print("Funker dette?")