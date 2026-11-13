"""Третья практика. Управление командой покемонов."""

from pokemon_api import get_pokemon, show_pokemon


def add_pokemon(team, name):
    """Добавить покемона, если его ещё нет в команде."""
    if name in team:
        print("Этот покемон уже в команде.")
        return

    pokemon = get_pokemon(name)
    if pokemon:
        name = pokemon["name"]
        if name in team:
            print("Этот покемон уже в команде.")
        else:
            team[name] = pokemon
            print(f"{name} добавлен в команду.")


def battle(team):
    """Сравнить характеристики двух покемонов из команды."""
    first = input("Имя первого покемона: ").strip().lower()
    second = input("Имя второго покемона: ").strip().lower()
    if first not in team or second not in team or first == second:
        print("Выберите двух разных покемонов из команды.")
        return

    # Сила покемона равна сумме его базовых характеристик.
    first_score = sum(stat["base_stat"] for stat in team[first]["stats"])
    second_score = sum(stat["base_stat"] for stat in team[second]["stats"])
    print(f"{first}: {first_score}, {second}: {second_score}")

    if first_score > second_score:
        print(f"Победил {first}.")
    elif second_score > first_score:
        print(f"Победил {second}.")
    else:
        print("Ничья.")


def main():
    """Запустить меню управления командой."""
    team = {}

    while True:
        print("\n1. Добавить покемона")
        print("2. Удалить покемона")
        print("3. Показать команду")
        print("4. Найти покемона по имени")
        print("5. Тренировочный бой")
        print("0. Выйти")
        command = input("Действие: ").strip()

        if command == "0":
            break

        if command in ("1", "2", "4"):
            name = input("Имя покемона: ").strip().lower()
            if not name:
                print("Введите имя покемона.")
                continue

        if command == "1":
            add_pokemon(team, name)
        elif command == "2":
            if name in team:
                del team[name]
                print(f"{name} удалён из команды.")
            else:
                print("Этого покемона нет в команде.")
        elif command == "3":
            if not team:
                print("Команда пуста.")
            for pokemon in team.values():
                show_pokemon(pokemon)
                print()
        elif command == "4":
            pokemon = team.get(name) or get_pokemon(name)
            if pokemon:
                show_pokemon(pokemon)
        elif command == "5":
            battle(team)
        else:
            print("Выберите пункт меню.")


if __name__ == "__main__":
    main()
