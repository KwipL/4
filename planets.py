import requests

response = requests.get('https://swapi.dev/api/')
planets_api = response.json()['planets']
response = requests.get(planets_api)
print(response.json())
