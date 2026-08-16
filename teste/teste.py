import pandas as pd
import numpy as np
import matplotlib as matplot

daniel = pd.DataFrame(
    {
        'A': [10,30,40,50],
        'B':[10,40,np.nan,30]
    }
    ,index=[1,2,3,4]
)
#print(daniel)

daniel2 = daniel.mean()

print(daniel2)