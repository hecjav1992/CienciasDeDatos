from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import requests

browser = webdriver.Chrome()
browser.get('http://www.umdmusic.com/default.asp?Lang=English&Chart=D')
artidt="LADY GAGA "
cantante=requests.get(f'https://api.deezer.com/artist/{artidt}')
#https://musicbrainz.org/ws/2/artist/?query=artist:Juanes&fmt=json
colum1 = []
colum2 = []
ranking=[]
lista=[]
lista2=[]
pp=browser.find_elements(By.CSS_SELECTOR,)
for tabla in browser.find_elements(By.CSS_SELECTOR, 'body > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > table:nth-child(6)'):
    for columnas in tabla.find_elements(By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td'):
        colum1.append(columnas.text.replace("\n", " "))
    for columnas2 in tabla.find_elements(By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td'):
        colum2.append(columnas2.text.replace("\n", " "))  
colum1.remove("This Week Statistics")
colum1.remove("Overall Statistics")
colum1.insert(2,colum2[0])
colum1.insert(3,colum2[1])
colum1.insert(5,colum2[2])
colum1.insert(6,colum2[3])
colum1.insert(7,colum2[4])
colum1.insert(8,colum2[5])
for tabla in browser.find_elements(By.CSS_SELECTOR, 'body > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > table:nth-child(6)'):
    filas = tabla.find_elements(By.CSS_SELECTOR, 'tbody > tr')  
#print(row2.find_elements(By.CSS_SELECTOR,'td:nth-child(5)'))






lista=[]
ranking=[]
lista2=[]
total=[]
artista = []
fecha=[]
ep=[]
tiempoM=[]
for row in filas[2:]:
    indice=1
    lista.append(row.find_elements(By.CSS_SELECTOR, f'td:nth-child(1)')[0].text)  
    ranking.append(row.find_elements(By.CSS_SELECTOR, 'td:nth-child(2)')[0].text)  
    lista2.append(row.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)')[0].text)
    total.append(row.find_elements(By.CSS_SELECTOR,'td:nth-child(4)')[0].text) 
    artista.append(row.find_elements(By.CSS_SELECTOR,'td:nth-child(5)')[0].text)
    fecha.append(row.find_elements(By.CSS_SELECTOR,'td:nth-child(6)')[0].text)
    ep.append(row.find_elements(By.CSS_SELECTOR,'td:nth-child(7)')[0].text)


dd = pd.DataFrame({
    colum1[0]: lista,
    colum1[1]: ranking,
    colum1[2]: lista2,
    colum1[3]: total,
    colum1[4]:artista,
    colum1[5]:fecha,
    colum1[6]:ep
})






   
