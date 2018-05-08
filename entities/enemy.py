import pygame
from constants import *


class Enemy(pygame.sprite.Sprite):
    # Inputs: (width, height), (x, y) ~ (red, green, blue)
    def __init__(self, dimensions, location, color=RED):
        pygame.sprite.Sprite.__init__(self)
        self.dimensions = dimensions
        self.width, self.height = dimensions
        self.spawn = location
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
        self.velocity_y = 0

    def update(self):
        self.pos_x += self.velocity_x
        self.pos_y -= self.velocity_y
        if self.velocity_y > 0:
            self.velocity_y -= .001
        else:
            self.velocity_y = 0
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def fall(self, rate):
        self.pos_y += rate

