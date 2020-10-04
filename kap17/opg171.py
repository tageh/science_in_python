import numpy as np 

sider = np.array(['Mynt', 'Kron'])
ss = 5
replace = True
prob = np.array([1/2,1/2])

kast = np.random.choice(sider,ss,replace,prob)

print(kast)

