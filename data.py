import kagglehub
import pandas as pd
import matplotlib.pyplot as mp
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

ruta = r"C:\Users\Easy Data\.cache\kagglehub\datasets\iabhishekofficial\mobile-price-classification\versions\1\train.csv"
df = pd.read_csv(ruta)
print(df.shape)
print(df.info())
print(df.columns)
print(df.describe())
carrelacion = df.corr(numeric_only=)
print(carrelacion)
sm.graphics.plot_corr(carrelacion, xnames=df.columns)
mp.show()
#print("la suma es ",df["battery_power"].duplicated().sum())
# Aplicar MinMaxScaler solo a las columnas numéricas
df_numeric = df.select_dtypes(include=['float64', 'int64'])
scaler = MinMaxScaler()
df_numeric_scaled = pd.DataFrame(scaler.fit_transform(df_numeric), columns=df_numeric.columns)
print(df_numeric_scaled)
X = df[['ram']] 
y = df['price_range'].values  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Coeficiente de determinación (R²): {r2:.2f}')
mp.scatter(X_test, y_test, color='blue', label='Datos reales')
mp.plot(X_test, y_pred, color='red', linewidth=2, label='Regresión Lineal')
mp.xlabel("RAM")
mp.ylabel("Rango de precio")
mp.title("Regresión Lineal: Precio vs RAM")
mp.legend()
mp.show()
nuevas_ram = [[500], [1000], [1500], [2000], [2500], [3000], [3500], [4000]]
predicciones = modelo.predict(nuevas_ram)
'''
for ram, precio in zip(nuevas_ram, predicciones):
    print(f'Predicción de precio para {ram[0]} MB RAM: {precio:.2f}')

ram2=[[18000]]
predicciones = modelo.predict(ram2)'
'''
print(f'{round(predicciones[3],2)}')
