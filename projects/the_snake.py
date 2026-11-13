"""Игра «Змейка» с управлением стрелками."""

from random import choice

import pygame

# Игровые координаты считаем в клетках. При рисовании умножаем их
# на размер клетки, чтобы получить координаты в пикселях.
CELL_SIZE = 20
COLUMNS = 32
ROWS = 24
SPEED = 20
START = (COLUMNS // 2, ROWS // 2)
RIGHT = (1, 0)
DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: RIGHT,
}


class GameObject:
    """Общий класс для объектов, которые рисуются на поле."""

    def __init__(self, color):
        """Запомнить цвет объекта."""
        self.color = color

    def draw_cell(self, screen, position):
        """Нарисовать одну клетку в цвете объекта."""
        # position — это (столбец, строка). Умножение на CELL_SIZE
        # даёт координаты верхнего левого угла квадрата в окне.
        x, y = position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, (93, 216, 228), rect, 1)


class Snake(GameObject):
    """Змейка, у которой есть список клеток и направление."""

    def __init__(self):
        """Задать цвет и начальное состояние змейки."""
        super().__init__((0, 255, 0))
        self.reset()

    def reset(self):
        """Вернуть змейку в центр и направить вправо."""
        # Голова находится в начале списка, хвост — в конце.
        # Длина змейки равна количеству клеток в списке.
        self.positions = [START]
        self.direction = RIGHT

    def turn(self, key):
        """Повернуть по стрелке и сообщить, был ли поворот."""
        direction = DIRECTIONS.get(key)
        dx, dy = self.direction
        # Противоположное направление получаем сменой знаков.
        # Повтор той же стрелки и нажатие другой клавиши игнорируем.
        if direction in (None, self.direction, (-dx, -dy)):
            return False
        self.direction = direction
        return True

    def move(self, apple_position):
        """Сделать один шаг и сообщить, пора ли сменить яблоко."""
        x, y = self.positions[0]
        dx, dy = self.direction
        # При выходе за границу остаток от деления переносит голову
        # на другой край. Например, -1 % 32 даёт 31.
        head = ((x + dx) % COLUMNS, (y + dy) % ROWS)
        ate_apple = head == apple_position

        # При обычном шаге хвост уйдёт, поэтому его клетка свободна
        # для новой головы. Если съели яблоко, хвост оставляем.
        if not ate_apple:
            self.positions.pop()

        # Если новая голова попала в оставшееся тело, начинаем заново
        # и просим поставить яблоко на новой свободной клетке.
        if head in self.positions:
            self.reset()
            return True

        self.positions.insert(0, head)
        return ate_apple

    def draw(self, screen):
        """Нарисовать все клетки змейки."""
        for position in self.positions:
            self.draw_cell(screen, position)


class Apple(GameObject):
    """Яблоко, которое появляется в свободной клетке."""

    def __init__(self, snake_positions):
        """Задать цвет и выбрать первую клетку для яблока."""
        super().__init__((255, 0, 0))
        self.randomize_position(snake_positions)

    def randomize_position(self, snake_positions):
        """Переместить яблоко на случайную свободную клетку."""
        # Перебираем все строки и столбцы. Сохраняем только клетки,
        # которых нет в списке координат змейки.
        free_cells = []
        for y in range(ROWS):
            for x in range(COLUMNS):
                if (x, y) not in snake_positions:
                    free_cells.append((x, y))

        # Если свободных клеток нет, None обозначает победу.
        self.position = None
        if free_cells:
            self.position = choice(free_cells)

    def draw(self, screen):
        """Нарисовать яблоко, если у него есть клетка."""
        if self.position is not None:
            self.draw_cell(screen, self.position)


def draw_field(screen, snake, apple):
    """Перерисовать поле целиком."""
    # Чёрный фон закрывает предыдущий кадр. Затем рисуем объекты
    # поверх него и показываем готовый кадр в окне.
    screen.fill((0, 0, 0))
    snake.draw(screen)
    apple.draw(screen)
    pygame.display.flip()


def main():
    """Открыть окно и запустить игровой цикл."""
    # Сначала открываем окно, затем создаём змейку и яблоко.
    pygame.init()
    screen = pygame.display.set_mode((COLUMNS * CELL_SIZE, ROWS * CELL_SIZE))
    pygame.display.set_caption("Змейка")
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple(snake.positions)
    draw_field(screen, snake, apple)

    while True:
        # Таймер ограничивает число шагов в секунду. За один шаг
        # принимаем максимум один поворот, даже при быстрых нажатиях.
        clock.tick(SPEED)
        turned = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and not turned:
                turned = snake.turn(event.key)

        # После победы оставляем последний кадр на экране.
        # Событие закрытия окна всё равно проверяется на каждом шаге.
        if apple.position is None:
            continue

        # Новое яблоко нужно после еды или после сброса змейки.
        if snake.move(apple.position):
            apple.randomize_position(snake.positions)
            if apple.position is None:
                pygame.display.set_caption("Победа! Всё поле заполнено")

        draw_field(screen, snake, apple)


# Окно открывается при запуске файла. Импорт позволяет брать классы
# и функции из этого файла отдельно, например для проверки.
if __name__ == "__main__":
    main()
