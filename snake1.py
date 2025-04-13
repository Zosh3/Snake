import pygame

from game_constants import SNAKE_SIZE, SNAKE_SPEED, SNAKE_DIRECTION_UP, SNAKE_DIRECTION_DOWN, SNAKE_DIRECTION_LEFT, SNAKE_DIRECTION_RIGHT, SNAKE_DIRECTION_NONE
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Snake1:
    """Class representing the snake in the game."""

    def __init__(self, colour, x, y):
        self.colour = colour
        self.x = x
        self.y = y
        self.size = SNAKE_SIZE
        self.speed = SNAKE_SPEED
        self.direction = SNAKE_DIRECTION_NONE

    def draw(self, screen):
        """Draw the snake on the screen."""
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.size, self.size])

    def move(self, dx, dy):
        """Move the snake in the specified direction."""
        self.x += dx * self.speed
        self.y += dy * self.speed

    def move2(self):
        """Move the snake in the specified direction."""
        if self.direction == SNAKE_DIRECTION_UP:
            self.y -= self.speed   
        elif self.direction == SNAKE_DIRECTION_DOWN:
            self.y += self.speed
        elif self.direction == SNAKE_DIRECTION_LEFT:
            self.x -= self.speed
        elif self.direction == SNAKE_DIRECTION_RIGHT:
            self.x += self.speed

    def is_on_screen(self):
        """Check if the snake is within the screen bounds."""
        return 0 <= self.x <= SCREEN_WIDTH - self.size and 0 <= self.y <= SCREEN_HEIGHT - self.size