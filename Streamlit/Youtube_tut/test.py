import pandas as pd
import numpy as np


df=pd.DataFrame(
    columns=["A","B"],
    data=np.random.randn(100,2)/[1,2000]
)

print(df)