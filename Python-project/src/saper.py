import pygame
import __main__
import map

class Saper(object):
    def __init__(self):
        # lokalizacja_startowa
        self.saper_x = 1
        self.saper_y = 1

        # szerokosc o dlugosc sapera
        self.saper_width = 32
        self.saper_height = 32

        # kierunek {"North" : 0, "South" : 1, "East" : 2, "West" : 3}
        self.direction = 0

        self.walk = False

        self.how = 0
        self.rect = pygame.Rect(self.saper_x * 32, self.saper_y * 32, self.saper_width, self.saper_height)

        self.bomb = False

    def Update(self):
        if self.walk == True:
            self.Walk()
        if self.bomb == True:
            __main__.bomb.rect.x = self.rect.x + __main__.bomb.bomb_width / 2
            __main__.bomb.rect.y = self.rect.y + __main__.bomb.bomb_height / 2


    def Render(self):
        pygame.draw.rect(__main__.gameDisplay, __main__.saper_color, self.rect)

    def Collision(self):
        for wall in __main__.walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == 2: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if self.direction == 3: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if self.direction == 1: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if self.direction == 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                #return True
        #return False

    def Move(self, meters):
        self.how = meters
        self.walk = True

    def Walk(self):
        if self.how != 0: #and self.Collision() == False:
            if self.direction == 0 and self.rect.y > 0:
                self.rect.y -= self.saper_height
            elif self.direction == 1 and self.rect.y < 448 - self.saper_height:
                self.rect.y += self.saper_height
            elif self.direction == 2 and self.rect.x < __main__.window_width - self.saper_width:
                self.rect.x += self.saper_width
            elif self.direction == 3 and self.rect.x > 0:
                self.rect.x -= self.saper_width
            else:
                self.how = 0
                self.walk = False
            self.how -= 1
        else:
            self.walk = False
        self.Collision()

    def Rotate(self):
        if self.direction == 0:
            self.direction = 2
        elif self.direction == 1:
            self.direction = 3
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 0
        self.walk = False
        print("Kierunek: %d" % self.direction)

    def Pick_up(self):
        if self.rect.colliderect(__main__.bomb):
            print("mam")
            self.bomb = True
        else:
            print("nie mam")