import pygame
import __main__

class Bomb:
    bomb_x = 500
    bomb_y = 500

    bomb_radius = 10
    bomb_width = 0

    #def Update(self):


    def Render(self):
        pygame.draw.circle(__main__.gameDisplay, __main__.green, [self.bomb_x, self.bomb_x], self.bomb_radius, self.bomb_width) #__main__