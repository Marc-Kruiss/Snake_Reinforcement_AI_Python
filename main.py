import pygame
import random
from collections import namedtuple
from enum import Enum

pygame.init()
font = pygame.font.Font("snake-chan.ttf", 25)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple('Point', 'x, y')

BLOCK_SIZE = 20
SPEED = 40

# rgb Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)


class SnakeGame:

    def __init__(self, w=640, h=480):
        self.w, self.h = w, h

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
                      ]
        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)

        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        # 1. collect user input

        # 2. move

        # 3. check if game over

        # 4. place new food or just move

        # 5. update ui and clock
        self._update_ui()
        # self._update_tick(SPEED)
        # 6. return game over and score
        game_over = False
        return game_over, self.score

    def _update_ui(self):
        self.display.fill(BLACK)

        # draw snake
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        # draw food
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()  # update full display to screen


if __name__ == '__main__':
    game = SnakeGame()

    # game loop
    while True:
        game_over, score = game.play_step()

        # break if game over
        if game_over == True:
            break

        [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

    print('Final Score', score)
    pygame.quit()
