import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

url='https://raw.githubusercontent.com/lorey/list-of-countries/master/csv/countries.csv'
df=pd.read_csv(url,sep=";")
print(df.head(5))
print('cantidad de filas y columnas ',df.shape)
print('nombre de las columnas',df.columns)
df.info()
print(df.describe())
corr=df.corr(numeric_only=True)
sm.graphics.plot_corr(corr,xnames=list(corr.columns))
plt.show()

df_español=df.replace(np.nan,'',regex=True)
df_español=df_español[df_español['languages'].str.contains('es')]
print(df_español)

#detencion de Outlier
#grafiquemps

df_español.set_index('alpha_3')[['population','area']].plot(kind='bar',rot=65,figsize=(220,10))
#data=df_español
plt.show()
anomalies=[]
def find_anomalies(data):
    data_std=data.std()
    data_mean=data.mean()
    anomalies_cut_off=data_std*2
    lower_limit=data_mean-anomalies_cut_off
    uper_limit=data_mean+anomalies_cut_off
    print(lower_limit.iloc[0])
    print(uper_limit.iloc[0])

    for index,row in data.iterrows():
        outlier=row
        if(outlier.iloc[0]>uper_limit.iloc[0]) or(outlier.iloc[0]<lower_limit[0]):
            anomalies.append(index)
    return anomalies

print(find_anomalies(df_español.set_index('alpha_3')[['population']]))
