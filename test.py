import requests
url = "http://localhost:3000/response"

response = requests.get(url)
res = response.json()
lista = res['results']
test = lista[0]
print(response.json())