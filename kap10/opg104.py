import pandas as pd 
import numpy as np 

df = pd.DataFrame(np.random.randn(7,3), columns = list('DEF'))

df['D*F'] = df.D * df.F

print(df)