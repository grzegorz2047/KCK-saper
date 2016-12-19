import pygame
import __main__

class Saper:
    #lokalizacja_startowa
    saper_x = 0
    saper_y = 0

    #szerokosc o dlugosc sapera
    saper_width = 32
    saper_height = 32

    #kierunek {"North" : 0, "South" : 1, "East" : 2, "West" : 3}
    direction = 0

    walk = False

    how = 0

    def Update(self):
        if self.walk == True:
            self.Walk()

    def Render(self):
        pygame.draw.rect(__main__.gameDisplay, __main__.red, [self.saper_x, self.saper_y, self.saper_width, self.saper_height]) # __main__

    def Move(self, meters):
        self.how = meters
        self.walk = True

    def Walk(self):
        if self.how != 0:
            if self.direction == 0 and self.saper_y > 0:
                self.saper_y -= self.saper_height
            elif self.direction == 1 and self.saper_y < 448 - self.saper_height:
                self.saper_y += self.saper_height
            elif self.direction == 2 and self.saper_x < __main__.window_width - self.saper_width: # __main__
                self.saper_x += self.saper_width
            elif self.direction == 3 and self.saper_x > 0:
                self.saper_x -= self.saper_width
            else:
                self.how = 0
                self.walk = False
            self.how -= 1
        else:
            self.walk = False

    def Rotate(self):
        if self.direction == 0:
            self.direction = 3
        elif self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 0
        elif self.direction == 3:
            self.direction = 1
        print("Kierunek: %d" % self.direction)



