from pprint import pprint
import requests

list_heroes = ['Thanos', 'Captain America', 'Hulk']
dict_heroes = {}


def get_int_hero():
    URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    params = {'name': 'Hulk'}
    response = requests.get(url=URL, params=params)
    for hero in response.json():
        if hero['name'] in list_heroes:
            dict_heroes[hero['name']] = hero['powerstats']['intelligence']


if __name__ == '__main__':
    get_int_hero()
    pprint(f'Самый умный герой из списка : {max(dict_heroes, key=dict_heroes.get)}')

