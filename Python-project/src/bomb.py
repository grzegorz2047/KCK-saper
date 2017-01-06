import pygame
import __main__

class Bomb(object):
    def __init__(self):
        self.bomb_x = 10
        self.bomb_y = 10

        self.bomb_width = 16
        self.bomb_height = 16

        self.type = 0 # randomowy typ bomby (do zrobienia)

        self.time_start = pygame.time.get_ticks()
        self.time_current = 0

        self.rect = pygame.Rect(self.bomb_x * 32 + self.bomb_width / 2, self.bomb_y * 32 + self.bomb_height / 2, self.bomb_width, self.bomb_height)

    def Update(self):
        #miganie bomby
        self.time_current = (pygame.time.get_ticks() - self.time_start)/1000 #sekundy
        if self.time_current % 2 == 0:
            self.color = __main__.bomb_color
        else:
            self.color = __main__.red

    def Render(self):
        #pygame.draw.circle(__main__.gameDisplay, self.color, [self.bomb_x * 32 + self.bomb_radius + self.bomb_radius / 2, self.bomb_y * 32 + self.bomb_radius + self.bomb_radius / 2], self.bomb_radius, self.bomb_width)
        pygame.draw.rect(__main__.gameDisplay, self.color, self.rect)