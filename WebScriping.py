import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime 
import pandas as pd

url_page = 'https://www.konzerta.com/empleos-busqueda-vendedor.html'
page = requests.get(url_page).text
soup = BeautifulSoup(page,"lxml")
p=soup.text
print(p)
'''
precios = [div.get_text(strip=True) for div in soup.find_all("div", class_="d3-ad-tile__price", recursive=True)]
dataframe = pd.DataFrame(precios, columns=['Precios'])
print(precios)
print(dataframe)
print(dataframe.dtypes)
print(dataframe.info())
print(dataframe.describe())
print("###############################################")
dataframe['Precios'] = dataframe['Precios'].replace(r'B/\.', '', regex=True)
dataframe['Precios'] = dataframe['Precios'].replace(r'-\d+%', '', regex=True)
dataframe['Precios'] = pd.to_numeric(dataframe['Precios'], errors='coerce')
print(dataframe.describe())
'''
'''
dataframe['Precios'] = dataframe['Precios'].replace(r'B/\.', '', regex=True)
dataframe['Precios'] = dataframe['Precios'].replace(r'-\d+%', '', regex=True)
dataframe['Precios'] = pd.to_numeric(dataframe['Precios'], errors='coerce')
print(dataframe.describe())
'''
''''
name=""
price=""
nroFila=0
for fila in tabla.find_all("tr"):
    if nroFila==1:
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==0:
                name=celda.text
                print("Indice:", name)
            if nroCelda==2:
                price=celda.text
                print("Valor:", price)
            nroCelda=nroCelda+1
    nroFila=nroFila+1
with open('bolsa_ibex35.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
url_page = 'https://www.lifeder.com/cientificos-famosos/'
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")
contenido = soup.find('div', attrs={'class': 'td-post-content'})
items = contenido.find_all('a')
for item in items:
    print(item['href'])
'''