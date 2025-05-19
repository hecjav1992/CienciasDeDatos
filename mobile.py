import kagglehub
import pandas as pd
import matplotlib.pyplot as mpl
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import  train_test_split
import statsmodels.api as st
import numpy as np
import scipy.stats as stats
#path = kagglehub.dataset_download("abdulmalik1518/mobiles-dataset-2025")
path=r"C:\Users\Easy Data\.cache\kagglehub\datasets\abdulmalik1518\mobiles-dataset-2025\versions\1\MobilesDataset(2025).csv"
df=pd.read_csv(path,encoding="latin1")
print(df)
print(df.shape)
print(df.info())
print(df.duplicated())
pd.set_option("display.max_rows",None)
print(df.duplicated().sum())
print(df.isna().sum())
print(df.columns)
df=df.drop_duplicates(keep="first").reset_index(drop=True)
print(df.duplicated().sum())
print(df.columns)
print(df.describe())
df["Mobile Weight"]=df["Mobile Weight"].str.replace("g"," ",regex=True).str.strip()
print(df["Mobile Weight"].dtype)
df["Mobile Weight"]=pd.to_numeric(df["Mobile Weight"]).astype(int)
print(df["Mobile Weight"].dtype)
print(df["Mobile Weight"])
print(df.describe())
atipico = []
data_std = df["Mobile Weight"].std()
data_mean = df["Mobile Weight"].mean()
anomaly_cut_off = data_std * 2
lower_limit = data_mean - anomaly_cut_off
upper_limit = data_mean + anomaly_cut_off
print(f"Límite inferior: {lower_limit}")
print(f"Límite superior: {upper_limit}")
atipico = df[(df["Mobile Weight"] < lower_limit) | (df["Mobile Weight"] > upper_limit)]["Mobile Weight"].tolist()
print("Valores atípicos:", atipico)
correlacion = df[["Mobile Weight", "Launched Year"]].corr()
print(correlacion)
print(sorted(atipico))
st.graphics.plot_corr(correlacion,xnames=correlacion.columns)
mpl.show()
mpl.figure(figsize=(12, 5))

mpl.subplot(1, 2, 1)
stats.histplot(df["Mobile Weight"], bins=30, kde=True, stat="density")
stats.title("Histograma y KDE")
edades=np.array(df["Mobile Weight"])
mpl.show()
edad_unique, counts = np.unique(edades, return_counts=True)
sizes = counts*100
colors = ['blue']*len(edad_unique)
colors[-1] = 'red'
mpl.axhline(1, color='k', linestyle='--')
mpl.scatter(edad_unique, np.ones(len(edad_unique)), s=sizes, color=colors)
mpl.yticks([])
mpl.show()
'''
Q1 = df["Mobile Weight"].quantile(0.25)
Q3 = df["Mobile Weight"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
atipico = df[(df["Mobile Weight"] < lower_limit) | (df["Mobile Weight"] > upper_limit)]["Mobile Weight"].tolist()
print("Valores atípicos (IQR):", atipico)
'''