import pandas as pd 
import numpy as np 

s1 = pd.Series(np.random.randn(10), name='values')

s1 = s1.sort_values()
row1 = s1.iloc[1]
print('liste med tall:', s1)
print(row1)
