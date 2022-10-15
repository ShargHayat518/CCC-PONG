import random

import pygame
# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')
powerup_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
green = (0, 255, 0)


def get_powerup_color():
    return powerup_color
