import pandas as pd 
import numpy as np

df1 = pd.DataFrame(np.random.randint(10,size=(12,3)), columns = list("ABC"))
df2 = pd.DataFrame(np.random.randint(10,size=(10,3)), columns = list("DEF"))

df = pd.concat([df1, df2], axis=1)



print(df.nunique())