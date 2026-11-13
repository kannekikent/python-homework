"""Запросы к PokéAPI и вывод характеристик покемона."""

import json
from functools import lru_cache
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

API_URL = "https://pokeapi.co/api/v2/pokemon/"


@lru_cache(maxsize=128)
def get_data(url):
    """Получить и сохранить в памяти ответ API."""
    request = Request(url, headers={"User-Agent": "PokemonPractice/1.0"})
    with urlopen(request, timeout=10) as response:
        return json.load(response)


def get_pokemon(name):
    """Найти покемона по имени или номеру."""
    try:
        return get_data(API_URL + quote(name, safe="") + "/")
    except HTTPError as error:
        if error.code == 404:
            print("Покемон не найден.")
        else:
            print(f"Ошибка PokéAPI: {error.code}")
    except (URLError, TimeoutError):
        print("Не удалось подключиться к PokéAPI.")


def show_pokemon(pokemon):
    """Вывести основные характеристики покемона."""
    types = [item["type"]["name"] for item in pokemon["types"]]
    abilities = [item["ability"]["name"] for item in pokemon["abilities"]]
    print(f"Имя: {pokemon['name']}")
    print(f"Тип: {', '.join(types)}")
    print(f"Вес: {pokemon['weight'] / 10:g} кг")
    print(f"Рост: {pokemon['height'] / 10:g} м")
    print(f"Способности: {', '.join(abilities)}")
