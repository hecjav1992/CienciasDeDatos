import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

url='https://raw.githubusercontent.com/DrueStaples08/Population_Growth/master/countries.csv'
df_pop=pd.read_csv(url,sep=",")
print(df_pop.head(5))
df_pop_es=df_pop[df_pop["country"]=='Spain']
print(df_pop_es.head())
df_pop_es.drop(['country'],axis=1)['population'].plot(kind='bar')
#plt.show()

df_pro_ar=df_pop[(df_pop['country']=='Argentina')]
anios=df_pop_es['year'].unique()
pop_ar=df_pro_ar['population'].values
pop_es=df_pop_es['population'].values

df_plot=pd.DataFrame({'Argentina':pop_ar,'Spain':pop_es},index=anios)
df_plot.plot(kind='bar')
plt.show()
print(df_pop.head())