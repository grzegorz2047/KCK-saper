import pygame
import __main__


class Wall(object):
    def __init__(self, pos):
        __main__.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
