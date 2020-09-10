import requests
import json


# address = 'Москва г.,Алабяна ул., д.10/1'

# получение коордита по адресу. На вход: адрес
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


def getcoordinates_from_excel(array):
    arr_pos = []
    for address in array:
        result_url = 'https://geocode-maps.yandex.ru/1.x/?apikey=d02c5ac9-442e-43a3-8f34-4b641f189db6&format=json&geocode=' + address
        response = requests.get(result_url)
        todos = json.loads(response.text)
        pos = todos['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        result = pos[1] + " " + pos[0]
        arr_pos.append(result)
    return arr_pos
