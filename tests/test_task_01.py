from homework.lesson_01.task_01 import greet


def test_greet() -> None:
    assert greet("Мир") == "Привет, Мир!"

