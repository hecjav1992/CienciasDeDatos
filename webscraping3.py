from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

browser = webdriver.Chrome()
browser.get('https://www.konzerta.com/empleos-busqueda-vendedor.html')
lista = []
vacante = []
empresa = []
ubicacion = []
salario = []
elems = browser.find_elements(By.CSS_SELECTOR, 'span>h3')
lista = [valores.text for valores in elems]
print(lista)
if lista:
    i = 0
    b = 1
    c = 2
    Psocicion = 2

    while i < len(lista):
        vacante.append(lista[i])
        empresa.append(lista[b])
        ubicacion.append(lista[c])

        try:
            check_input = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'#listado-avisos > div:nth-child({Psocicion}) > a'))
            )
            browser.execute_script("arguments[0].scrollIntoView();", check_input)
            time.sleep(1)  # Esperar para evitar bloqueos
            browser.execute_script("arguments[0].click();", check_input)
            time.sleep(2)
            browser.switch_to.window(browser.window_handles[1])

            elemPsocicion = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#ficha-detalle'))
            )
            salario.append(elemPsocicion.text)
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
        except Exception as e:
            print(f"Error al procesar la vacante en posición {Psocicion}: {e}")
            salario.append("Error")
        i += 4
        b += 4
        c += 4
        Psocicion += 1
else:
    print("No se encontraron elementos.")
input("Presiona Enter para cerrar...")
browser.quit()
df_vacante = pd.DataFrame(vacante, columns=["vacantes"])
df_empresas = pd.DataFrame(empresa, columns=["empresas"])
df_ubicacion = pd.DataFrame(ubicacion, columns=["ubicacion"])
df_salario = pd.DataFrame(salario, columns=["salario"])
dataframetotal = pd.concat([df_vacante, df_empresas, df_ubicacion, df_salario], axis=1)
print(dataframetotal)
dataframetotal.to_excel("archivo.xlsx")
print(dataframetotal.columns)

