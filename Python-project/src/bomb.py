import pygame
import __main__
import random

class Bomb(object):
    def __init__(self):
        self.bomb_x = random.randint(1, 16)
        self.bomb_y = random.randint(10, 17)

        self.bomb_width = 16
        self.bomb_height = 16

        self.active = 1

        self.type = random.randint(1, 3) # randomowy typ bomby (do zrobienia)

        self.disarmed = False
        self.defused = False

        if self.type == 1: #mozna rozbroic, mozna podniesc
            self.lifting = True
            self.disarming = True
        elif self.type == 2: #nie mozna rozbroic, mozna podniesc
            self.lifting = True
            self.disarming = False
        elif self.type == 3: #mozna rozbroic, nie mozna podniesc
            self.lifting = False
            self.disarming = True

        self.time_start = pygame.time.get_ticks()
        self.time_current = 0

        self.rect = pygame.Rect(self.bomb_x * 32 + self.bomb_width / 2, self.bomb_y * 32 + self.bomb_height / 2, self.bomb_width, self.bomb_height)

    def Reset(self):
        self.type = random.randint(1, 3)
        if self.type == 1: #mozna rozbroic, mozna podniesc
            self.lifting = True
            self.disarming = True
        elif self.type == 2: #nie mozna rozbroic, mozna podniesc
            self.lifting = True
            self.disarming = False
        elif self.type == 3: #mozna rozbroic, nie mozna podniesc
            self.lifting = False
            self.disarming = True
        self.active = 1
        self.bomb_x = random.randint(1, 16)
        self.bomb_y = random.randint(10, 17)
        __main__.saper.to_find_bomb = True
        __main__.saper.to_answer = False
        self.defused = False
        self.rect = pygame.Rect(self.bomb_x * 32 + self.bomb_width / 2, self.bomb_y * 32 + self.bomb_height / 2,
                                self.bomb_width, self.bomb_height)


    def Update(self):
        #miganie bomby
        self.time_current = (pygame.time.get_ticks() - self.time_start)/1000 #sekundy
        if self.time_current % 2 == 0:
            self.color = __main__.bomb_color
        elif self.defused == False:
            if self.type == 1 and self.disarmed == False:
                self.color = __main__.red
            elif self.type == 2:
                self.color = __main__.blue
            elif self.type == 3 and self.disarmed == False:
                self.color = __main__.yellow

    def Render(self):
        pygame.draw.rect(__main__.gameDisplay, self.color, self.rect)

    def Detonate(self):
        for wall in __main__.strefa_detonacji:
            if self.rect.colliderect(wall.rect):
                self.active = 0
                self.rect.x = -1 * 32
                self.rect.y = -1 * 32
                return True
        return False