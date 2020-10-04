import pandas as pd
import numpy as np 

df = pd.DataFrame(data = {'col1': [1.0,2.0], 'col2': [3.0, 4.0]})

#print(df)
#print( df + 10)
#print( df *df)

a = df.to_numpy()

print('a: ', a)
print('a+10: ', a + 10)
print('a*a: ' ,a *a)

