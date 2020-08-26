import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return x**2 + 3

def g(x):
    return 3*x -1

xa = np.linspace(-2,3, 100)

plt.figure(1, figsize=(12,9))
plt.xlabel("x aksen")
plt.ylabel("y asksen")
plt.plot(xa, f(xa),xa , g(xa))
plt.legend(labels=('f(x)', 'g(x)'))
plt.show()
