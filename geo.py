import requests
import json


# address = 'Москва г.,Алабяна ул., д.10/1'

def getcoordinates(address):
    if address:
        key = 'd02c5ac9-442e-43a3-8f34-4b641f189db6'
        url = 'https://geocode-maps.yandex.ru/1.x/?apikey=' + key + '&format=json&geocode=' + address
        response = requests.get(url)
        todos = json.loads(response.text)
        pos = todos['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        return pos[1] + " " + pos[0]
    else:
        return None
