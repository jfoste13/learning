import pygame, sys
from constants import *
from entities.ground import *
from entities.player import *
from entities.enemy import *
from entities.fireball import *
from physics.gravity import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # images
    PLAYER_IMAGE = pygame.image.load('entities/player/player.png').convert_alpha()

    # training objects
    entities_static = pygame.sprite.Group()
    entities_dynamic = pygame.sprite.Group()
    entities_projectiles = pygame.sprite.Group()
    platform_main = Ground((580, 60), (70, 580), BLACK)
    player = Player((20, 60), (SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 2), PLAYER_IMAGE)
    enemy = Enemy((20, 50), (SCREEN_SIZE[0] / 1.5, SCREEN_SIZE[1] / 2))
    entities_static.add(platform_main)
    entities_dynamic.add(player)
    entities_dynamic.add(enemy)

    # physics objects
    gravity = GravityManager(.5)
    gravity.terrain = entities_static
    gravity.entities = entities_dynamic
    grounded = []

    while True:
        # event handling
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                sys.exit()
        # -- player controls
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.velocity_x = -.5
                elif event.key == pygame.K_d:
                    player.velocity_x = .5
                elif event.key == pygame.K_w:
                    if player in grounded:
                        player.velocity_y = 1.1
                    if player.flying:
                        player.velocity_y = .5
                elif event.key == pygame.K_s:
                    if player.flying:
                        player.velocity_y = -.5
                elif event.key == pygame.K_e:
                    player.teleport('RIGHT')
                elif event.key == pygame.K_q:
                    player.teleport('LEFT')
                elif event.key == pygame.K_f:
                    player.flying = not player.flying
                elif event.key == pygame.K_SPACE:
                    fireball = Fireball((8, 8), (player.pos_x + 15, player.pos_y + 30), player.facing)
                    entities_projectiles.add(fireball)
            elif event.type is pygame.KEYUP:
                if event.key == pygame.K_a and player.velocity_x < 0:
                    player.velocity_x = 0
                elif event.key == pygame.K_d and player.velocity_x > 0:
                    player.velocity_x = 0
                elif event.key == pygame.K_w:
                    if player.flying:
                        player.velocity_y = 0
                elif event.key == pygame.K_s:
                    if player.flying:
                        player.velocity_y = 0

        # logic
        grounded = gravity.ground_entities()
        for entity in entities_dynamic:
            if entity not in grounded:
                entity.fall(gravity.g)
        entities_dynamic.update()
        entities_static.update()
        entities_projectiles.update()
        # rendering
        screen.fill(WHITE)
        entities_static.draw(screen)
        entities_dynamic.draw(screen)
        entities_projectiles.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
