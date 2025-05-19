import requests

# Lista de jugadores (puedes agregar más jugadores)
jugadores = [
    "Marcos_Llorente", "Lionel_Messi", "Cristiano_Ronaldo", "Neymar", 
    "Kylian_Mbappé", "Mohamed_Salah", "Sergio_Ramos", "Paul_Pogba", 
    "Harry_Kane", "Virgil_van_Dijk"
]

# Función para obtener la información de los futbolistas
def obtener_info_futbolista(jugador):
    # Formamos la URL de la API con el nombre del jugador
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={jugador}"
    
    try:
        # Realizamos la solicitud a la API
        response = requests.get(url)
        data = response.json()

        # Verificamos si se encontraron jugadores
        if data['player']:
            # Extraemos los datos del primer jugador en la lista
            jugador_info = data['player'][0]
            nombre = jugador_info['strPlayer']
            fecha_nacimiento = jugador_info['dateBorn']
            sexo = jugador_info['strGender']
            
            return f"Nombre: {nombre}, Fecha de Nacimiento: {fecha_nacimiento}, Sexo: {sexo}"
        else:
            return f"No se encontraron datos para {jugador}"
    except Exception as e:
        return f"Error al obtener datos: {str(e)}"

# Consultamos la información de cada jugador
for jugador in jugadores:
    info_futbolista = obtener_info_futbolista(jugador)
    print(info_futbolista)
