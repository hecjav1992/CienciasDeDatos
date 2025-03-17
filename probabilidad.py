import enum
import random

# Definimos el Enum para representar los posibles valores de un niño
class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

# Función para generar un niño aleatorio
def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

# Inicializamos los contadores
both_girls = 0
older_girl = 0
either_girl = 0

# Fijamos la semilla para reproducibilidad
random.seed(0)

# Realizamos las simulaciones
for _ in range(10):
    younger = random_kid()
    older = random_kid()
    print(younger)
    print(older)
    
    if older == Kid.GIRL:
        older_girl += 1
        
    if younger == Kid.GIRL:
        both_girls += 1
    
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

# Calculamos las probabilidades
prob_both_given_older = both_girls / older_girl
prob_both_given_either = both_girls / either_girl

# Imprimimos los resultados
print("P(both | older):", prob_both_given_older)  # Debería ser cercano a 1/2
print("P(both | either):", prob_both_given_either)  # Debería ser cercano a 1/3