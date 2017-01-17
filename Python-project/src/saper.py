import pygame
import __main__
import text

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
        self.head = pygame.Rect(self.saper_x * 32 + 8, self.saper_y * 32, self.saper_width / 2, self.saper_height / 2)
        self.rect = pygame.Rect(self.saper_x * 32, self.saper_y * 32, self.saper_width, self.saper_height)

        self.bomb = False
        self.bylo = False

    def Update(self):
        if self.walk == True:
            self.Walk()
        if self.bomb == True:
            __main__.bomb.rect.x = self.rect.x + __main__.bomb.bomb_width / 2
            __main__.bomb.rect.y = self.rect.y + __main__.bomb.bomb_height / 2
        if self.direction == 0:
            self.head.x = self.rect.x + 8
            self.head.y = self.rect.y
        elif self.direction == 2:
            self.head.x = self.rect.x + 16
            self.head.y = self.rect.y + 8
        elif self.direction == 1:
            self.head.x = self.rect.x + 8
            self.head.y = self.rect.y + 16
        elif self.direction == 3:
            self.head.x = self.rect.x
            self.head.y = self.rect.y + 8

        if __main__.chat.saved_function_name == "Pojedz" and self.walk == False and __main__.chat.found_number == True:
            self.Rotate_dir(__main__.chat.saved_parameter_name)
            self.Move(__main__.chat.saved_number)
            __main__.chat.saved_function_name = ""
            __main__.chat.saved_parameter_name = ""
            __main__.chat.saved_number = 0
            __main__.chat.found_number = False
        elif __main__.chat.saved_function_name == "Pojedz" and self.bylo == False and self.walk == False:
            __main__.chat.chat_log.append(text.Text("O ile kratek mam sie przemiescic?", __main__.chat.saper_color))
            self.bylo = True

        if __main__.chat.saved_function_name == "Podnies" and  __main__.chat.saved_object_name == "Bomba":
            if self.Pick_up() != True and self.bylo == False:
                __main__.chat.chat_log.append(text.Text("Nie jestem w zasiegu bomby.", __main__.chat.saper_color))
                self.bylo = True
            elif self.Pick_up():
                __main__.chat.chat_log.append(text.Text("Mam.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
                __main__.chat.saved_object_name = ""

        elif __main__.chat.saved_function_name == "Podnies" and self.bylo == False:
            __main__.chat.chat_log.append(text.Text("Nie wiem co mam podniesc.", __main__.chat.saper_color))
            self.bylo = True

        if __main__.chat.saved_function_name == "Obroc":
            if self.Rotate_dir(__main__.chat.saved_parameter_name):
                __main__.chat.chat_log.append(text.Text("Obrocilem sie.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
                __main__.chat.saved_parameter_name = ""
            elif self.bylo == False:
                __main__.chat.chat_log.append(text.Text("W ktora strone mam sie obrocic?", __main__.chat.saper_color))
                self.bylo = True

        if len(__main__.chat.chat_log) > 4:
            __main__.chat.chat_log.pop(0)

    def Render(self):
        pygame.draw.rect(__main__.gameDisplay, __main__.saper_color, self.rect)
        pygame.draw.rect(__main__.gameDisplay, __main__.saper_head, self.head)

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

    def Move(self, meters):
        self.how = meters
        self.walk = True

    def Walk(self):
        if self.how != 0: #and self.Collision() == False:
            if self.direction == 0:
                self.rect.y -= self.saper_height
            elif self.direction == 1:
                self.rect.y += self.saper_height
            elif self.direction == 2:
                self.rect.x += self.saper_width
            elif self.direction == 3:
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

    def Rotate_dir(self, direction):
        if(direction == 'Lewo'):
            self.direction = 3
            return True
        elif (direction == 'Prawo'):
            self.direction = 2
            return True
        elif (direction == 'Dol'):
            self.direction = 1
            return True
        elif (direction == 'Przod'):
            return True
        elif (direction == 'Gora'):
            self.direction = 0
            return True
        elif (direction == 'Tyl'):
            if (self.direction == 1):
                self.direction = 0;

            elif (self.direction == 2):
                self.direction = 3;

            elif (self.direction == 0):
                self.direction = 1;

            elif (self.direction == 3):
                self.direction = 2;

            return True
        return False



    def Pick_up(self):
        if self.rect.colliderect(__main__.bomb) and __main__.bomb.lifting == True:
            self.bomb = True
            return True
        return False

    def Drop(self):
        if self.bomb == True:
            self.bomb = False