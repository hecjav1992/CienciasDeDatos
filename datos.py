import requests

url = "https://www.carqueryapi.com/api/0.3/?cmd=getTrims&make=toyota&year=2020"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error en la solicitud:", response.status_code, response.text)
