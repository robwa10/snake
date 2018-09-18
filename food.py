import pygame
from pygame.sprite import Sprite
from random import randint


class Food(Sprite):
    """A class to manage the snake food on the screen."""

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.food_width,
                                settings.food_height)
        self.rect.centerx = randint(5, 1195)
        self.rect.centery = randint(5, 795)

        self.y = float(self.rect.y)

        self.color = settings.food_color

    def draw_food(self):
        """Draw the food to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
