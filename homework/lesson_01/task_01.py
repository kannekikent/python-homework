"""Пример первого задания."""


def greet(name: str) -> str:
    """Вернуть приветствие для пользователя."""
    return f"Привет, {name}!"


if __name__ == "__main__":
    user_name = input("Как вас зовут? ")
    print(greet(user_name))

