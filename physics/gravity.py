import pygame


class GravityManager():
    def __init__(self, g=1):
        self.terrain = None
        self.entities = None
        self.g = g

    # returns every sprite that should be falling
    def ground_entities(self):
        grounded = pygame.sprite.Group()
        for entity in self.entities:
            for solid in self.terrain:
                if pygame.sprite.collide_rect(entity, solid):
                    grounded.add(entity)
        return grounded
