import kagglehub
import pandas as pd
import matplotlib.pyplot as mpl
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import  train_test_split
import statsmodels.api as st
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
atipico=[]
data_std = df["Mobile Weight"].std()
data_mean = df["Mobile Weight"].mean()
anomaly_cut_off = data_std * 2
lower_limit  = data_mean - anomaly_cut_off 
upper_limit = data_mean + anomaly_cut_off
print(lower_limit)
print(upper_limit)
for index in df["Mobile Weight"]:
        outlier = index
        if (outlier > upper_limit) or (outlier < lower_limit):
            atipico.append(index)
correlacion = df[["Mobile Weight", "Launched Year"]].corr()
print(correlacion)
print(sorted(atipico))
st.graphics.plot_corr(correlacion,xnames=correlacion.columns)
mpl.show()
