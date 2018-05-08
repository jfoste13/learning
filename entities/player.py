import pygame
from main import *
from constants import *


class Player(pygame.sprite.Sprite):
    # Inputs: (width, height), (x, y), image
    def __init__(self, dimensions, location, image):
        pygame.sprite.Sprite.__init__(self)
        self.dimensions = dimensions
        self.width, self.height = dimensions
        self.location = location
        self.pos_x, self.pos_y = location

        # create the image
        self.image = pygame.Surface(self.dimensions)
        self.image = image
        self.image_right = image
        self.image_left = pygame.transform.flip(self.image, True, False)

        # create the rectangle
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        # motion attributes
        self.velocity_x = 0
        self.velocity_y = 0
        self.facing = 'RIGHT'
        self.flying = False

    def update(self):
        self.pos_x += self.velocity_x
        self.pos_y -= self.velocity_y
        if not self.flying:
            if self.velocity_y > 0:
                self.velocity_y -= .001
            else:
                self.velocity_y = 0
        if self.velocity_x > 0:
            self.image = self.image_right
            self.facing = 'RIGHT'
        elif self.velocity_x < 0:
            self.image = self.image_left
            self.facing = 'LEFT'
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def teleport(self, direction, distance=100):
        if direction is 'RIGHT':
            self.pos_x += distance
        elif direction is 'LEFT':
            self.pos_x -= distance

    def fall(self, rate):
        if not self.flying: self.pos_y += rate
