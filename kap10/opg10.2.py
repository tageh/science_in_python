import pandas as pd 
import numpy as np 

s1 = pd.Series(np.random.randn(600))

s1 = s1.iloc[100:400]

s1.plot.hist()

