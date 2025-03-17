#####################################################
##### Indentifiacion de patrones####################
##### Ciencias de Datos###############################
#####################################################
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
#Inicializar el dict con una lista vacía para cada id de usuario:
print(friendship_pairs)
friendships = {user["id"]:[]  for user in users}
print(friendships)

# Y pasar por todos los pares de amistad para llenarlo:
for i, j in friendship_pairs:
 friendships[i].append(j) # Añadir j como un amigo del usuario i
 friendships[j].append(i) # Añadir i como un amigo del usuario j
print("aqui", friendships)
print(friendships)
def number_of_friends(user):
 user_id = user["id"]
 print("##################################################")
 print(user_id)
 friend_ids = friendships[user_id]
 print(friend_ids)
 print(len(friend_ids))
 return len(friend_ids)
##print(list(number_of_friends(user)for user in users))
print("################### resultado""""""""""""""""""""""""")
total_connections = sum(number_of_friends(user)for user in users)
cantidades=list(number_of_friends(user)for user in users)
num_users = len(users) # longitud de la lista de usuarios
avg_connections = total_connections /num_users
print("#################################")
print(cantidades)
print(total_connections)
print(num_users)
print(avg_connections)
print("#################################")
# Crea una lista (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)


######################################3
##### Amigos de mis amigos############
######################################
def  foaf_ids_bad(user):
    return [foaf_id    #[]
        for friend_id in friendships[user["id"]]#[1,2]
        for foaf_id in friendships[friend_id]] #[0,2,3] 2=[0,1,3]


print("####################################")
print(foaf_ids_bad(users[0]) )
print("####################################")
print(friendships[0]) # [1, 2]
print(friendships[1]) # [0, 2, 3]
print(friendships[2]) # [0, 1, 3]"""


from collections import Counter # no cargado inicialmente
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id 
        for friend_id in friendships[user_id] # Para cada uno de mis amigos,
        for foaf_id in friendships[friend_id] # encuentra sus amigo
        if foaf_id != user_id # que no son y
        and foaf_id not in friendships[user_id]
    )
print(friends_of_friends(users[0])) # Contador({0: 2, 5: 1})
