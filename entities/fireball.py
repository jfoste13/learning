import pygame
from constants import *


class Fireball(pygame.sprite.Sprite):
    # Inputs: (width, height), (x, y), (left/right) ~ (red, green, blue)
    def __init__(self, dimensions, location, direction, color=ORANGE):
        pygame.sprite.Sprite.__init__(self)
        self.dimensions = dimensions
        self.width, self.height = dimensions
        self.location = location
        self.pos_x, self.pos_y = location
        self.color = color

        # create the image
        self.image = pygame.Surface(self.dimensions)
        self.image.fill(self.color)

        # create the rectangle
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        # motion attributes
        self.velocity_x = 0
        if direction == 'RIGHT':
            self.velocity_x = .5
        elif direction == 'LEFT':
            self.velocity_x = -.5

    def update(self):
        self.pos_x += self.velocity_x
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
