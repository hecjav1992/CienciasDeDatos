import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime 
import pandas as pd
from lxml import etree 


url_page = 'https://www.konzerta.com/empleos-busqueda-vendedor.html'
url=requests.get(url_page).text
soup=BeautifulSoup(url,'lxml')

dom = etree.HTML(str(soup)) 
valor=dom.xpath('/html/body/div[1]/div/div[3]/div[1]/div/div/div[2]/div[1]/a/div/div[1]/div[1]/div[2]/span/h3/text()')
print(valor)

valor=dom.xpath('//*[@id="currentlistings"]/div[2]/div[3]/div[2]/a/div[2]/span/text()')
elemento = dom.xpath('//*[@id="currentlistings"]/div[2]/div[4]')
contador=1 
while True:
    valor = dom.xpath(f'//*[@id="currentlistings"]/div[2]/div[{contador}][not(contains(@class, "ann-ad-tile"))]/div[2]/a/div[2]/span/text()')
    if valor !=[""]:
        print(dom.xpath(f'//*[@id="currentlistings"]/div[2]/div[{contador}]/div[2]/a/div[2]/span/text()')," ",contador)
        contador+=1
    else:
        break

