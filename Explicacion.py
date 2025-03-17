import pandas as pd
import openpyxl as xls
excel='C:/Users/Easy Data/Dropbox/PC/Desktop/ITSE/DATA SIENCE/practica1bd.xlsx'
hoja="Empleados"
df=pd.read_excel(excel,sheet_name=hoja)
#print(df)
diccionario=df.to_dict(orient='records')
#(diccionario)

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

amistades=[]
temporal=[]
comexion=[]
respuesta=0
def personas(users):
    for user in users:
        Id_personas=user["id"]
        temporal.clear()
        for i,j in friendship_pairs:
            
            if Id_personas==i:
                temporal.append(j)
                #amistades.append[j]
            elif Id_personas==j:
                temporal.append(i)
                #amistades.append[i]
            amistades=temporal
        comexion.append(len(temporal))
            
        print(Id_personas)
        print(amistades)
        print(len(amistades))
    print(comexion)
    respuesta=sum(comexion)/len(comexion)
    print(respuesta)
        
    return Id_personas

print(personas(users))
