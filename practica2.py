users = [{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
#Inicializar el dict con una lista vacía para cada id de usuario:
amistades={}
for user in users:
    amistades[user["id"]]=[]

conexiosn=[]
tamconecion=[]
tuplas2=[]
friendships = {user["id"]:[]  for user in users}
for user in users:
    temporal=[]
    print(user["id"])
    for i,j in  friendship_pairs:
        if user["id"]==i or user["id"]==j:
            if user["id"]!=i:
                conexiosn.append(i)
            elif user["id"]!=j:
                conexiosn.append(j)
    print(conexiosn) 
    temporal+=conexiosn
    amistades[user["id"]]=temporal
    print(len(conexiosn))  
    #print(amistades)
    tamconecion.append(len(conexiosn))
    conexiosn.clear()
print(tamconecion)
print("ttal de conexion",len(tamconecion))
print(sum(tamconecion))
print("media de conexion",sum(tamconecion)/len(tamconecion))
print(users[2]["name"])

from collections import Counter # no cargado inicialmente
def friends_of_friends(user):
    user_id = user["id"]
    print(user_id)
    return Counter(
        foaf_id 
        for friend_id in amistades[user_id] # Para cada uno de mis amigos,
        for foaf_id in amistades[friend_id] # encuentra sus amigo
        if foaf_id != user_id # que no son y
        and foaf_id not in amistades[user_id]
    )
print(friends_of_friends(users[3])) # Contador({0: 2, 5: 1})
listadoAmigos=[]
def name(user):
    IdUsuario=user["id"]
    print(IdUsuario)
    for amigo in amistades[IdUsuario]:
        print(amigo)
        for i,j in friendship_pairs:
            if amigo==i or amigo==j:
                    if i==amigo:
                        listadoAmigos.append(j)
                    elif j==amigo:
                        listadoAmigos.append(i)
        print(listadoAmigos)
    conteo = Counter(listadoAmigos)
    print(conteo)
    eliminar = amistades[IdUsuario]                
    nuevo_conteo = Counter({k: v for k, v in conteo.items() if k not in eliminar})
    return nuevo_conteo

print(name(users[3]))
#print(users[3])
#print("esta imprecion es amistades ",amistades)
                

        
 

#print(name(users[3],friendship_pairs))
#print(amistades[3])





#print(amistades[1])
#print(amistades[0])
#print(amistades[1])
#print(amistades[3])



    
     



