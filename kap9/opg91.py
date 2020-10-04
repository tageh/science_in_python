import numpy as np 

lotto = np.loadtxt('lotto.txt', delimiter=" ")

nr2 = np.count_nonzero(lotto == 2)

print("Tallet 2 går igjen",nr2,"ganger")