"""Сохранённый пример графической игры «Крестики-нолики»."""

# # game.py
# from unittest import result
# from gamess import Board
# from gamess.exceptions import CellOccupiedError, FieldIndexError
# # game.py
# import pygame
# # Здесь нужно импортировать класс Board. Импорт исключений для игры
# # с графическим интерфейсом не понадобится.
#
# pygame.init()
#
# # Здесь определены разные константы, например
# # размер ячейки и доски, цвет и толщина линий.
# # Эти константы используются при отрисовке графики.
# CELL_SIZE = 100
# BOARD_SIZE = 3
# WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
# LINE_WIDTH = 15
# BG_COLOR = (28, 170, 156)
# LINE_COLOR = (23, 145, 135)
# X_COLOR = (84, 84, 84)
# O_COLOR = (242, 235, 211)
# X_WIDTH = 15
# O_WIDTH = 15
# SPACE = CELL_SIZE // 4
#
# # Настройка экрана.
# # Задать размер графического окна для игрового поля.
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # Установить заголовок окна.
# pygame.display.set_caption('Крестики-нолики')
# # Заполнить фон окна заданным цветом.
# screen.fill(BG_COLOR)
#
#
# # Функция, которая отвечает за отрисовку горизонтальных и вертикальных линий.
# def draw_lines():
#     # Горизонтальные линии.
#     for i in range(1, BOARD_SIZE):
#         pygame.draw.line(
#             screen,
#             LINE_COLOR,
#             (0, i * CELL_SIZE),
#             (WIDTH, i * CELL_SIZE),
#             LINE_WIDTH
#         )
#
#     # Вертикальные линии.
#     for i in range(1, BOARD_SIZE):
#         pygame.draw.line(
#             screen,
#             LINE_COLOR,
#             (i * CELL_SIZE, 0),
#             (i * CELL_SIZE, HEIGHT),
#             LINE_WIDTH
#         )
#
#
# # Функция, которая отвечает за отрисовку фигур
# # (крестиков и ноликов) на доске.
# def draw_figures(board):
#     for row in range(BOARD_SIZE):
#         for col in range(BOARD_SIZE):
#             if board[row][col] == 'X':
#                 pygame.draw.line(
#                     screen,
#                     X_COLOR,
#                     (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
#                     (
#                         col * CELL_SIZE + CELL_SIZE - SPACE,
#                         row * CELL_SIZE + CELL_SIZE - SPACE
#                     ),
#                     X_WIDTH
#                 )
#                 pygame.draw.line(
#                     screen,
#                     X_COLOR,
#                     (
#                         col * CELL_SIZE + SPACE,
#                         row * CELL_SIZE + CELL_SIZE - SPACE
#                     ),
#                     (
#                         col * CELL_SIZE + CELL_SIZE - SPACE,
#                         row * CELL_SIZE + SPACE
#                     ),
#                     X_WIDTH
#                 )
#             elif board[row][col] == 'O':
#                 pygame.draw.circle(
#                     screen,
#                     O_COLOR,
#                     (
#                         col * CELL_SIZE + CELL_SIZE // 2,
#                         row * CELL_SIZE + CELL_SIZE // 2
#                     ),
#                     CELL_SIZE // 2 - SPACE,
#                     O_WIDTH
#                 )
#
#
# # Сюда нужно добавить функцию save_result().
# def save_result(result):
#     with open('results.txt', 'a', encoding='utf-8') as file:
#         file.write(result + '\n')
#
#
# # В этой функции описана логика игры. Вам нужно её дополнить. По структуре
# # тут всё то же самое, что было в вашем коде раньше.
# # Но есть отличие - вместо метода display() используется
# # новая функция draw_figures().
# def main():
#     game = Board()
#     current_player = 'X'
#     running = True
#     game_over = False
#     clock = pygame.time.Clock()
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 break
#
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 # После конца партии ходы запрещены.
#                 # Ходить можно только левой кнопкой мыши.
#                 if game_over or event.button != 1:
#                     continue
#
#                 mouse_x, mouse_y = event.pos
#                 clicked_col = mouse_x // CELL_SIZE
#                 clicked_row = mouse_y // CELL_SIZE
#
#                 if not (
#                     0 <= clicked_row < BOARD_SIZE
#                     and 0 <= clicked_col < BOARD_SIZE
#                 ):
#                     continue
#
#                 # В занятую клетку ходить нельзя.
#                 if game.board[clicked_row][clicked_col] in ('X', 'O'):
#                     continue
#
#                 # Записываем ход в поле.
#                 game.board[clicked_row][clicked_col] = current_player
#
#                 # Проверяем результат ПОСЛЕ хода.
#                 if game.check_win(current_player):
#                     result = f'Победили {current_player}.'
#                     print(result)
#                     save_result(result)
#                     pygame.display.set_caption(result)
#                     game_over = True
#
#                 elif game.is_board_full():
#                     result = 'Ничья!'
#                     print(result)
#                     save_result(result)
#                     pygame.display.set_caption(result)
#                     game_over = True
#
#                 else:
#                     current_player = (
#                         'O' if current_player == 'X' else 'X'
#                     )
#
#         if not running:
#             break
#
#         # Рисуем и показываем поле на каждом кадре.
#         screen.fill(BG_COLOR)
#         draw_lines()
#         draw_figures(game.board)
#         pygame.display.update()
#
#         # Ограничиваем частоту кадров.
#         clock.tick(60)
#
# if __name__ == '__main__':
#     main()
# pygame.quit()
