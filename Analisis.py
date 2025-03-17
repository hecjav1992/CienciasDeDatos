'''
1.1.2 Identificación de Tendencias

Al analizar grandes volúmenes de datos, se pueden hacer visibles 
tendencias que antes eran invisibles, y esta información puede utilizarse 
en diversos campos. Por ejemplo, en el ámbito de la salud, el análisis de 
datos de pacientes puede ayudar a identificar patrones y factores de riesgo
 que antes no se reconocían, lo que permite mejorar la prevención y las 
 estrategias de tratamiento.

En el ámbito financiero, el análisis de datos del mercado puede ayudar 
a los inversores a tomar decisiones más informadas y anticipar cambios 
en el mercado. Además, el análisis de datos también se puede utilizar 
para identificar áreas de mejora en las empresas, como el comportamiento 
y las preferencias de los clientes.

Esta información puede utilizarse para mejorar las estrategias de marketing 
y el desarrollo de productos, lo que conduce a un aumento de los ingresos y 
la satisfacción del cliente. Por lo tanto, el análisis de datos es cada vez 
más importante en muchos campos, ya que proporciona información valiosa que 
puede conducir a una mejor toma de decisiones y mejores resultados.
'''
import pandas as pd

customer_data = pd.read_csv("customer_data.csv")

most_frequent_category = customer_data['Purchase_Category'].value_counts().idxmax()

print(f"The most frequently purchased category is {most_frequent_category}.")

'''
---

1.1.1 Toma de Decisiones Informada

El análisis de datos es una herramienta esencial que permite a los responsables 
de la toma de decisiones tomar decisiones informadas y basadas en datos.
 Al analizar los datos del comportamiento del cliente, una empresa puede 
 identificar tendencias clave, preferencias y patrones que pueden ayudar 
 a desarrollar estrategias de marketing efectivas.

Además, el análisis de datos puede ayudar a identificar áreas de oportunidad 
que antes podían haber pasado desapercibidas. Esto puede ayudar a las empresas 
a mantenerse competitivas en el mercado al tomar decisiones informadas basadas 
en datos concretos en lugar de la intuición.

Asimismo, el análisis de datos puede ayudar a las empresas a identificar 
riesgos y desafíos potenciales, permitiéndoles prepararse y mitigar cualquier
posible impacto negativo. Esto garantiza que las empresas puedan operar de 
manera más efectiva y eficiente, maximizando su retorno de inversión.
'''
# Example code to analyze weather trends
import numpy as np
import matplotlib.pyplot as plt

# Simulated historical weather data (temperature in Fahrenheit)
years = np.arange(1980, 2021)
temperatures = np.random.normal(loc=70, scale=10, size=len(years))

# Plotting the data
plt.plot(years, temperatures)
plt.xlabel('Year')
plt.ylabel('Temperature (F)')
plt.title('Historical Weather Data')
plt.show()
'''
---

1.1.3 Mejora de la Eficiencia

Automatizar el análisis de datos puede tener un impacto profundo en la 
velocidad y eficiencia de la recopilación e interpretación de datos.
Al automatizar este proceso, no solo se reduce el tiempo dedicado al
análisis de datos, sino que también se garantiza que los datos se
recopilen e interpreten con precisión, lo que lleva a una toma
de decisiones más efectiva.
Esto es especialmente importante en campos críticos como la atención médica,
donde un análisis de datos rápido y preciso puede marcar la diferencia en 
términos de salvar vidas. Con la capacidad de automatizar el análisis de datos, 
los profesionales de la salud pueden identificar y diagnosticar enfermedades con
mayor facilidad, rastrear la propagación de enfermedades y desarrollar nuevos 
tratamientos.
Esto puede conducir a mejores resultados de salud 
para los pacientes y un uso más eficiente de los recursos sanitarios, 
beneficiando en última instancia a la sociedad en su conjunto.
'''
# Example code to analyze healthcare data
health_data = pd.read_csv("health_data.csv")

# Identifying high-risk patients based on certain conditions
high_risk_patients = health_data[(health_data['Blood_Pressure'] > 140)]

print(f"Number of high-risk patients: {len(high_risk_patients)}")