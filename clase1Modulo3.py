import pandas as pd
import numpy as np
from scipy import stats

df=pd.DataFrame({
    "Nombre":[np.nan,"carlos",np.nan],
    "Edad":[23,22,43],
    "Notas":[30,np.nan,80]

})

print(df.shape) #(3,3)
print(df.info()) # 1 y 3 columans 

df.fillna(0)
df.loc["Notas"].fillna(df.loc["Notas"].mean())
df.dropna()#1
df.replace("","S/N").astype(str)#3


df=pd.DataFrame({
    "A":[1,2,2,3,3,3],
    "B":[4,5,5,6,6,6],
    "C":[7,8,8,8,9,9]
})
datos=np.array([1,2,2,2,3,1,2,3,3,4,4,4,20])

print(df.describe(include="all"))
print(df.info())
print(df["Nombre"].duplicated())# true
print(df.duplicated()) #false
print(df.dropna())
print(df.drop_duplicates())
df=pd.DataFrame(datos)
z_scores=stats.zscore(datos)
outliers=np.abs(z_scores)>2
dataclean= df[~outliers]
print(dataclean)
'''
1+2+2+2+3+1+2+3+3+4+4+4+20/13= 31/13≈3.92 promedio
desviacion standar ≈4.63
formula zscore
1-3.92/4.63=-0.63
20-3.92/4.63=3.47
'''