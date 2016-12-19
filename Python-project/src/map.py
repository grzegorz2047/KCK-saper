import pygame
import __main__
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

    def Render(self):
        for y in xrange(self.height):
            for x in xrange(self.width):
                if int(self.data[x + y * self.width]) == 1:
                    pygame.draw.rect(__main__.gameDisplay, __main__.white, [x * 32, y * 32, 32, 32]) # do zmiany to z __main__
                if int(self.data[x + y * self.width]) == 2:
                    pygame.draw.rect(__main__.gameDisplay, __main__.black, [x * 32, y * 32, 32, 32]) # do zmiany to z __main__

