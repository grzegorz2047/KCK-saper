import pygame
import __main__
import text
import math

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
        self.to_find_bomb = True
        self.to_answer = False
        self.answer = False
        self.answer1 = False
        self.answer2 = False
        self.answer3 = False

    def Update(self):
        if self.to_find_bomb == True:
            self.Find_bomb()
        if self.answer == True:
            self.Move_to_bomb()
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

        self.Polecenia(); #Wykonywanie polecen

    def Polecenia(self):
        #wykonywanie polecen
        if self.to_answer == True:
            if __main__.chat.saved_function_name == "Zaprzeczenie":
                __main__.chat.chat_log.append(text.Text("Ok.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
                self.to_answer = False

            if __main__.chat.saved_function_name == "Zgoda":
                __main__.chat.chat_log.append(text.Text("Jade do niej.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
                self.to_answer = False
                self.answer = True
        elif self.answer1 == True:
            if __main__.chat.saved_function_name == "Podnies":
                self.Pick_up()
                self.answer1 = False
                __main__.chat.chat_log.append(text.Text("Ale ciezka.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
            elif __main__.chat.saved_function_name == "Rozbroj":
                self.Defuse(__main__.bomb)
                self.answer1 = False
                __main__.chat.chat_log.append(text.Text("Sie robi.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
            elif __main__.chat.saved_function_name == "Zaprzeczenie":
                self.answer1 = False
                __main__.chat.chat_log.append(text.Text("Nie to nie.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
        elif self.answer2 == True:
            if __main__.chat.saved_function_name == "Podnies" or __main__.chat.saved_function_name == "Zgoda":
                self.Pick_up()
                self.answer2 = False
                __main__.chat.chat_log.append(text.Text("Gotowe.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
        elif self.answer3 == True:
            if __main__.chat.saved_function_name == "Rozbroj" or __main__.chat.saved_function_name == "Zgoda":
                self.Defuse(__main__.bomb)
                self.answer3 = False
                __main__.chat.chat_log.append(text.Text("Uff, zyje!", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""

        elif __main__.chat.saved_function_name == "Pojedz" and self.walk == False and __main__.chat.found_number == True:
            self.Rotate_dir(__main__.chat.saved_parameter_name)
            self.Move(__main__.chat.saved_number)
            __main__.chat.saved_function_name = ""
            __main__.chat.saved_parameter_name = ""
            __main__.chat.saved_number = 0
            __main__.chat.found_number = False
        elif __main__.chat.saved_function_name == "Pojedz" and self.bylo == False and self.walk == False:
            __main__.chat.chat_log.append(text.Text("O ile kratek mam sie przemiescic?", __main__.chat.saper_color))
            self.bylo = True

        elif __main__.chat.saved_function_name == "Podnies" and  __main__.chat.saved_object_name == "Bomba" and self.Pick_up():
            __main__.chat.chat_log.append(text.Text("Podnioslem.", __main__.chat.saper_color))
            __main__.chat.saved_function_name = ""
            __main__.chat.saved_object_name = ""

        elif __main__.chat.saved_function_name == "Podnies" and self.bylo == False:
            __main__.chat.chat_log.append(text.Text("Nie wiem co mam podniesc.", __main__.chat.saper_color))
            self.bylo = True

        elif __main__.chat.saved_function_name == "Obroc":
            if self.Rotate_dir(__main__.chat.saved_parameter_name):
                __main__.chat.chat_log.append(text.Text("Obrocilem sie.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
                __main__.chat.saved_parameter_name = ""
            elif self.bylo == False:
                __main__.chat.chat_log.append(text.Text("W ktora strone mam sie obrocic?", __main__.chat.saper_color))
                self.bylo = True

        elif __main__.chat.saved_function_name == "Upusc":
            if self.Drop() == True:
                __main__.chat.chat_log.append(text.Text("Gotowe.", __main__.chat.saper_color))
                __main__.chat.saved_function_name = ""
            elif self.bylo == False:
                self.bylo = True
                __main__.chat.chat_log.append(text.Text("Nie mam co upuscic.", __main__.chat.saper_color))

        elif __main__.chat.saved_function_name == "Rozbroj" and  __main__.chat.saved_object_name == "Bomba":
            self.Defuse(__main__.bomb)
            __main__.chat.chat_log.append(text.Text("Rozborilem.", __main__.chat.saper_color))
            __main__.chat.saved_function_name = ""
            __main__.chat.saved_object_name = ""
        elif __main__.chat.saved_function_name == "Rozbroj" and self.bylo == False:
            __main__.chat.chat_log.append(text.Text("Nie wiem co mam rozbroic.", __main__.chat.saper_color))
            self.bylo = True
        elif __main__.chat.dont_understand:
            __main__.chat.chat_log.append(text.Text("Nie rozumiem chinskiego.", __main__.chat.saper_color))
            __main__.chat.dont_understand = False

        while len(__main__.chat.chat_log) > 9:
            __main__.chat.chat_log.pop(0)
        ###############################################################################################################3


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
                __main__.chat.chat_log.append(text.Text("Twarda sciana.", __main__.chat.saper_color))
                #if len(__main__.chat.chat_log) > 10:
                    #__main__.chat.chat_log.pop(0)
                self.walk = False

    def Move(self, meters):
        self.how = meters
        self.walk = True

    def Walk(self):
        if self.how != 0:
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

    def Distance(self, object):
        return math.sqrt(pow(object.x / 32 - self.rect.x / 32, 2) + pow(object.y / 32 - self.rect.y / 32, 2))

    #(math.fabs(self.rect.x - __main__.bomb.rect.x) / 32 < 8 and int(self.rect.y / 32) == int(__main__.bomb.rect.y / 32)) or (math.fabs(self.rect.y - __main__.bomb.rect.y) / 32 < 8 and int(self.rect.x / 32) == int(__main__.bomb.rect.x / 32))

    def Find_bomb(self):
        if  self.Distance(__main__.bomb.rect) < 6 and self.Distance(__main__.bomb.rect) > 1 and self.walk == False:
            self.to_find_bomb = False
            self.to_answer = True
            __main__.chat.chat_log.append(text.Text("Zauwazylem bombe, podjechac do niej?", __main__.chat.saper_color))

    def Move_to_bomb(self):
        x1 = self.rect.x / 32
        x2 = __main__.bomb.rect.x / 32
        y1 = self.rect.y / 32
        y2 = __main__.bomb.rect.y / 32
        if self.Distance(__main__.bomb.rect) > 1:
            if x1 < x2:
                self.direction = 2
                self.rect.x += self.saper_width
            elif x1 > x2:
                self.direction = 3
                self.rect.x -= self.saper_width
            elif y1 > y2:
                self.direction = 0
                self.rect.y -= self.saper_height
            elif y1 < y2:
                self.direction = 1
                self.rect.y += self.saper_height
        else:
            self.answer = False
            if __main__.bomb.type == 1:
                __main__.chat.chat_log.append(text.Text("Podniesc ja, a moze rozbroic?", __main__.chat.saper_color))
                self.answer1 = True
            elif __main__.bomb.type == 2:
                __main__.chat.chat_log.append(text.Text("Mam podniesc bombe?", __main__.chat.saper_color))
                self.answer2 = True
            elif __main__.bomb.type == 3:
                __main__.chat.chat_log.append(text.Text("Sprobowac rozbroic?", __main__.chat.saper_color))
                self.answer3 = True


    def Pick_up(self):
        if self.Distance(__main__.bomb.rect) <= 1 and __main__.bomb.lifting == True:
            self.bomb = True
            return True
        elif self.bylo == False:
            if self.Distance(__main__.bomb.rect) > 1:
                __main__.chat.chat_log.append(text.Text("Nie mam tak dlugich raczek.", __main__.chat.saper_color))
            elif __main__.bomb.lifting == False:
                __main__.chat.chat_log.append(text.Text("Nie moge podniesc tej bomby.", __main__.chat.saper_color))
            self.bylo = True
        return False

    def Drop(self):
        if self.bomb == True:
            self.bomb = False
            return True
        return False

    def Defuse(self, bomb):
        if (bomb.type == 1 or bomb.type == 3) and self.Distance(__main__.bomb.rect) <= 1:
            bomb.defused = True
        elif self.bylo == False and bomb.type == 2:
            __main__.chat.chat_log.append(text.Text("Nie moge rozbroic tej bomby.", __main__.chat.saper_color))
            self.bylo = True
        else:
            __main__.chat.chat_log.append(text.Text("Musze byc blizej bomby.", __main__.chat.saper_color))
            self.bylo = True

    #def Detonate(self, bomb):
