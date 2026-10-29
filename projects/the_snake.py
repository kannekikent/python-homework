"""Игра «Змейка»: управление стрелками, выход — закрытие окна."""

from random import choice

import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SPEED = 20
BORDER_COLOR = (93, 216, 228)

# Переменные сохранены на уровне модуля согласно прекоду задания.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


class GameObject:
    """Базовый объект с позицией и цветом."""

    def __init__(self):
        """Разместить объект в центре игрового поля."""
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self):
        """Определить интерфейс отрисовки для дочерних классов."""
        pass


class Apple(GameObject):
    """Яблоко, появляющееся в свободной клетке."""

    def __init__(self, occupied=()):
        """Задать цвет и выбрать начальную позицию яблока."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position(occupied)

    def randomize_position(self, occupied=()):
        """Выбрать свободную клетку; при заполненном поле задать None."""
        occupied = set(occupied)
        free_cells = [
            (col * GRID_SIZE, row * GRID_SIZE)
            for row in range(GRID_HEIGHT)
            for col in range(GRID_WIDTH)
            if (col * GRID_SIZE, row * GRID_SIZE) not in occupied
        ]
        self.position = choice(free_cells) if free_cells else None

    def draw(self):
        """Нарисовать яблоко, если для него есть место."""
        if self.position is not None:
            rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Змейка, представленная списком координат от головы к хвосту."""

    def __init__(self):
        """Создать зелёную змейку длиной в одну клетку."""
        super().__init__()
        self.body_color = SNAKE_COLOR
        self.reset()

    def update_direction(self):
        """Применить выбранное направление и очистить ожидающий поворот."""
        if self.next_direction is not None:
            self.direction = self.next_direction
        self.next_direction = None

    def move(self):
        """Добавить новую голову и запомнить удалённый конец хвоста."""
        x, y = self.get_head_position()
        dx, dy = self.direction
        new_head = (
            (x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (y + dy * GRID_SIZE) % SCREEN_HEIGHT,
        )
        self.positions.insert(0, new_head)
        self.last = None
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        self.position = new_head

    def draw(self):
        """Стереть след хвоста и нарисовать все сегменты змейки."""
        if self.last is not None:
            pygame.draw.rect(
                screen,
                BOARD_BACKGROUND_COLOR,
                pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE)),
            )
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    def get_head_position(self):
        """Вернуть координаты головы змейки."""
        return self.positions[0]

    def reset(self):
        """Вернуть змейку в центр и направить вправо."""
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None


def handle_keys(snake):
    """Обработать выход и один допустимый поворот за игровой шаг."""
    directions = {
        pygame.K_UP: UP,
        pygame.K_DOWN: DOWN,
        pygame.K_LEFT: LEFT,
        pygame.K_RIGHT: RIGHT,
    }
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN and event.key in directions:
            new_direction = directions[event.key]
            opposite = (-snake.direction[0], -snake.direction[1])
            if (
                snake.next_direction is None
                and new_direction != opposite
                and new_direction != snake.direction
            ):
                snake.next_direction = new_direction
    return True


def main():
    """Создать окно и выполнять игровые шаги до его закрытия."""
    global screen

    pygame.init()
    try:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Змейка')
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake = Snake()
        apple = Apple(snake.positions)
        won = False

        snake.draw()
        apple.draw()
        pygame.display.update()

        while True:
            clock.tick(SPEED)
            if not handle_keys(snake):
                break
            if won:
                continue

            snake.update_direction()
            snake.move()

            if snake.get_head_position() in snake.positions[1:]:
                snake.reset()
                apple.randomize_position(snake.positions)
                screen.fill(BOARD_BACKGROUND_COLOR)

            elif snake.get_head_position() == apple.position:
                snake.length += 1
                # Возвращаем хвост: рост виден уже на этом шаге.
                if snake.last is not None:
                    snake.positions.append(snake.last)
                    snake.last = None
                apple.randomize_position(snake.positions)
                if apple.position is None:
                    won = True
                    pygame.display.set_caption('Победа! Всё поле заполнено')

            snake.draw()
            apple.draw()
            pygame.display.update()
    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
