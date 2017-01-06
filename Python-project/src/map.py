import pygame
import __main__
import wall
import linecache

class Map:

    width = 0
    height = 0

    count = 0

    data = []
    amount = 0

    def Load(self, file_name):
        file = open(file_name + ".txt")
        try:
            for lane in file:
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
            file.close()
            for y in xrange(self.height):
                for x in xrange(self.width):
                    if int(self.data[x + y * self.width]) == 1:
                        wall.Wall((x * 32, y * 32))

    def Render(self):
        for y in xrange(self.height):
            for x in xrange(self.width):
                if int(self.data[x + y * self.width]) == 1:
                    #wall.Wall((x * 32, y * 32))
                    #pygame.draw.rect(__main__.gameDisplay, __main__.black, [x * 32, y * 32, 32, 32]) #wall
                    for wall in __main__.walls:
                        pygame.draw.rect(__main__.gameDisplay, __main__.black, wall.rect)
                if int(self.data[x + y * self.width]) == 2:
                    pygame.draw.rect(__main__.gameDisplay, __main__.white, [x * 32, y * 32, 32, 32])