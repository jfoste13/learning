import pygame
from constants import *


class Ground(pygame.sprite.Sprite):
    # Inputs: (width, height), (x, y) ~ (red, green, blue)
    def __init__(self, dimensions, location, color=BLACK):
        pygame.sprite.Sprite.__init__(self)
        self.dimensions = dimensions
        self.width, self.height = dimensions
        self.location = location
        self.pos_x, self.pos_y = location
        self.color = color

        # create the image of the ground
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(self.color)

        # create the rectangle
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
