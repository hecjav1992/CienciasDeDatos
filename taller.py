import random
import matplotlib.pyplot as plt

# Simulación de 30 lanzamientos de un dado
dados = [random.randint(1, 6) for _ in range(30)]

# Cálculo de frecuencia relativa
frecuencia = {i: dados.count(i) / 30 for i in range(1, 7)}

# Gráfico de barras
plt.bar(frecuencia.keys(), frecuencia.values(), color='skyblue', edgecolor='black')
plt.xlabel('Número del dado')
plt.ylabel('Frecuencia relativa')
plt.title('Simulación de Lanzamiento de un Dado (30 veces)')
plt.xticks(range(1, 7))
plt.show()
