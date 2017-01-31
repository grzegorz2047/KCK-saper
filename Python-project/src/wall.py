import pygame
import __main__


class Wall(object):
    walls = []  # lista scian

    def __init__(self, pos):
        self.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
