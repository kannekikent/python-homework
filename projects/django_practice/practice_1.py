"""Первая практика. Просмотр покемонов через PokéAPI."""

from urllib.error import URLError

from pokemon_api import API_URL, get_data, get_pokemon, show_pokemon


def main():
    """Показать первые двадцать покемонов и данные выбранного покемона."""
    try:
        data = get_data(API_URL + "?limit=20")
    except (URLError, TimeoutError):
        print("Не удалось получить список покемонов.")
        return

    for number, pokemon in enumerate(data["results"], start=1):
        print(f"{number}. {pokemon['name']}")

    name = input("Имя покемона: ").strip().lower()
    if name:
        pokemon = get_pokemon(name)
        if pokemon:
            show_pokemon(pokemon)


if __name__ == "__main__":
    main()
