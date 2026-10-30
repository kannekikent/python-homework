"""Модель игрового поля для игры «Крестики-нолики»."""


class Board:
    """Поле размером три на три с проверкой результата партии."""

    def __init__(self):
        """Создать пустое игровое поле размером три на три."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.field_size = 3

    def make_move(self, row, col, player):
        """Записать символ игрока в ячейку по указанным индексам."""
        self.board[row][col] = player

    def display(self):
        """Вывести игровое поле с разделителями в консоль."""
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_board_full(self):
        """Проверить, что на игровом поле нет свободных ячеек."""
        # Цикл проходится по всем строкам игрового поля.
        for i in range(self.field_size):
            # А потом по всем столбцам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == " ":
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

    def check_win(self, player):
        """Проверить линии и диагонали на победу указанного игрока."""
        # Проверка по горизонталям и вертикалям.
        for i in range(self.field_size):
            if all(
                [self.board[i][j] == player for j in range(self.field_size)]
            ) or all(
                [self.board[j][i] == player for j in range(self.field_size)]
            ):
                return True

        # Проверка по диагоналям
        if all(
            [self.board[i][i] == player for i in range(self.field_size)]
        ) or all(
            [
                self.board[i][self.field_size - 1 - i] == player
                for i in range(self.field_size)
            ]
        ):
            return True

        return False

    def __str__(self):
        """Вернуть текстовое описание размеров игрового поля."""
        return (
            "Объект игрового поля размером "
            f"{self.field_size}x{self.field_size}"
        )
