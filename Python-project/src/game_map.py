import pygame

import __main__
from wall import Wall


class GameMap:
    def __init__(self, game_logic_arg, game_display_arg):
        self.game_logic = game_logic_arg
        self.game_display = game_display_arg

    width = 0
    height = 0

    count = 0

    data = []
    amount = 0

    def load(self, file_name):
        map_file = open(file_name + ".txt")
        try:
            for lane in map_file:
                lane.strip()
                lane.split()
                if self.count == 0:
                    self.width = int(lane)
                    self.count += 1
                elif self.count == 1:
                    self.height = int(lane)
                    self.count += 1
                else:
                    for word in lane:
                        if word != '\n':
                            self.data.append(word)
        finally:
            self.amount = self.width * self.height
            map_file.close()
            for y in xrange(self.height):
                for x in xrange(self.width):
                    if int(self.data[x + y * self.width]) == 1:
                        self.walls = Wall((x * 32, y * 32))

    def render(self):
        for y in xrange(self.height):
            for x in xrange(self.width):
                if int(self.data[x + y * self.width]) == 1:
                    for game_wall in self.walls.walls:
                        pygame.draw.rect(self.game_display, self.game_logic.colors.black, game_wall.rect)
                elif int(self.data[x + y * self.width]) == 2:
                    pygame.draw.rect(self.game_display, self.game_logic.colors.floor, [x * 32, y * 32, 32, 32])
                elif int(self.data[x + y * self.width]) == 3:
                    pygame.draw.rect(self.game_display, self.game_logic.colors.green, [x * 32, y * 32, 32, 32])
                elif int(self.data[x + y * self.width]) == 4:
                    pygame.draw.rect(self.game_display, self.game_logic.colors.gray, [x * 32, y * 32, 32, 32])
