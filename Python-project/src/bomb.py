import pygame
import __main__
import random


class Bomb(object):
    def __init__(self, game_logic_arg, game_display_arg):
        self.game_display = game_display_arg
        self.game_logic = game_logic_arg
        self.bomb_x = 10
        self.bomb_y = 10

        self.bomb_width = 16
        self.bomb_height = 16

        self.type = random.randint(1, 3)  # randomowy typ bomby (do zrobienia)

        self.disarmed = False
        self.defused = False

        if self.type == 1:  # mozna rozbroic, mozna podniesc
            self.lifting = True
            self.disarming = True
        elif self.type == 2:  # nie mozna rozbroic, mozna podniesc
            self.lifting = True
            self.disarming = False
        elif self.type == 3:  # mozna rozbroic, nie mozna podniesc
            self.lifting = False
            self.disarming = True

        self.time_start = pygame.time.get_ticks()
        self.time_current = 0

        self.rect = pygame.Rect(self.bomb_x * 32 + self.bomb_width / 2, self.bomb_y * 32 + self.bomb_height / 2,
                                self.bomb_width, self.bomb_height)

    def Update(self):
        # miganie bomby
        self.time_current = (pygame.time.get_ticks() - self.time_start) / 1000  # sekundy
        if self.time_current % 2 == 0:
            self.color = self.game_logic.bomb_color
        elif not self.defused:
            if self.type == 1 and not self.disarmed :
                self.color = self.game_logic.red
            elif self.type == 2:
                self.color = self.game_logic.blue
            elif self.type == 3 and not self.disarmed:
                self.color = self.game_logic.yellow

    def Render(self):
        pygame.draw.rect(self.game_display, self.color, self.rect)
