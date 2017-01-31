import pygame
import __main__
import text
import math


class Saper(object):
    def __init__(self, game_logic_arg):
        # lokalizacja_startowa
        self.game_logic = game_logic_arg
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

    def update(self):
        if self.to_find_bomb:
            self.find_bomb()
        if self.answer:
            self.move_to_bomb()
        if self.walk:
            self.walk()
        if self.bomb:
            self.game_logic.bomb.rect.x = self.rect.x + self.game_logic.bomb.bomb_width / 2
            self.game_logic.bomb.rect.y = self.rect.y + self.game_logic.bomb.bomb_height / 2
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

        self.polecenia()  # Wykonywanie polecen

    def polecenia(self):
        # wykonywanie polecen
        if self.to_answer:
            if self.game_logic.chat.saved_function_name == "Zaprzeczenie":
                self.game_logic.chat.chat_log.append(text.Text("Ok.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
                self.to_answer = False

            if self.game_logic.chat.saved_function_name == "Zgoda":
                self.game_logic.chat.chat_log.append(text.Text("Jade do niej.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
                self.to_answer = False
                self.answer = True
        elif self.answer1:
            if self.game_logic.chat.saved_function_name == "Podnies":
                self.pick_up()
                self.answer1 = False
                self.game_logic.chat.chat_log.append(text.Text("Ale ciezka.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
            elif self.game_logic.chat.saved_function_name == "Rozbroj":
                self.Defuse(self.game_logic.bomb)
                self.answer1 = False
                self.game_logic.chat.chat_log.append(text.Text("Sie robi.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
            elif self.game_logic.chat.saved_function_name == "Zaprzeczenie":
                self.answer1 = False
                self.game_logic.chat.chat_log.append(text.Text("Nie to nie.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
        elif self.answer2:
            if self.game_logic.chat.saved_function_name == "Podnies" or self.game_logic.chat.saved_function_name == "Zgoda":
                self.pick_up()
                self.answer2 = False
                self.game_logic.chat.chat_log.append(text.Text("Gotowe.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
        elif self.answer3 == True:
            if self.game_logic.chat.saved_function_name == "Rozbroj" or self.game_logic.chat.saved_function_name == "Zgoda":
                self.Defuse(self.game_logic.bomb)
                self.answer3 = False
                self.game_logic.chat.chat_log.append(text.Text("Uff, zyje!", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
        elif self.game_logic.chat.saved_function_name == "Zaprzeczenie":
            self.game_logic.chat.saved_function_name = ""
            self.game_logic.chat.saved_parameter_name = ""
            self.game_logic.chat.saved_number = 0
            self.game_logic.chat.found_number = False
            self.game_logic.chat.chat_log.append(
                text.Text("Nie wykonam rozkazu poprzedzonego zaprzeczeniem", self.game_logic.chat.saper_color))
        elif self.game_logic.chat.saved_function_name == "Pojedz" and self.walk == False and self.game_logic.chat.found_number == True:
            self.rotate_dir(self.game_logic.chat.saved_parameter_name)
            self.move(self.game_logic.chat.saved_number)
            self.game_logic.chat.saved_function_name = ""
            self.game_logic.chat.saved_parameter_name = ""
            self.game_logic.chat.saved_number = 0
            self.game_logic.chat.found_number = False
        elif self.game_logic.chat.saved_function_name == "Pojedz" and self.bylo == False and self.walk == False:
            self.game_logic.chat.chat_log.append(
                text.Text("O ile kratek mam sie przemiescic?", self.game_logic.chat.saper_color))
            self.bylo = True

        elif self.game_logic.chat.saved_function_name == "Podnies" and self.game_logic.chat.saved_object_name == "Bomba" and self.pick_up():
            self.game_logic.chat.chat_log.append(text.Text("Podnioslem.", self.game_logic.chat.saper_color))
            self.game_logic.chat.saved_function_name = ""
            self.game_logic.chat.saved_object_name = ""

        elif self.game_logic.chat.saved_function_name == "Podnies" and self.bylo == False:
            self.game_logic.chat.chat_log.append(
                text.Text("Nie wiem co mam podniesc.", self.game_logic.chat.saper_color))
            self.bylo = True

        elif self.game_logic.chat.saved_function_name == "Obroc":
            if self.rotate_dir(self.game_logic.chat.saved_parameter_name):
                self.game_logic.chat.chat_log.append(text.Text("Obrocilem sie.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
                self.game_logic.chat.saved_parameter_name = ""
            elif not self.bylo:
                self.game_logic.chat.chat_log.append(
                    text.Text("W ktora strone mam sie obrocic?", self.game_logic.chat.saper_color))
                self.bylo = True

        elif self.game_logic.chat.saved_function_name == "Upusc":
            if self.drop():
                self.game_logic.chat.chat_log.append(text.Text("Gotowe.", self.game_logic.chat.saper_color))
                self.game_logic.chat.saved_function_name = ""
            elif not self.bylo:
                self.bylo = True
                self.game_logic.chat.chat_log.append(text.Text("Nie mam co upuscic.", self.game_logic.chat.saper_color))

        elif self.game_logic.chat.saved_function_name == "Rozbroj" and self.game_logic.chat.saved_object_name == "Bomba":
            self.Defuse(self.game_logic.bomb)
            self.game_logic.chat.chat_log.append(text.Text("Rozborilem.", self.game_logic.chat.saper_color))
            self.game_logic.chat.saved_function_name = ""
            self.game_logic.chat.saved_object_name = ""
        elif self.game_logic.chat.saved_function_name == "Rozbroj" and self.bylo == False:
            self.game_logic.chat.chat_log.append(
                text.Text("Nie wiem co mam rozbroic.", self.game_logic.chat.saper_color))
            self.bylo = True
        elif self.game_logic.chat.dont_understand:
            self.game_logic.chat.chat_log.append(text.Text("Nie rozumiem.", self.game_logic.chat.saper_color))
            self.game_logic.chat.dont_understand = False

        while len(self.game_logic.chat.chat_log) > 9:
            self.game_logic.chat.chat_log.pop(0)
            # ##############################################################################################################3

    def render(self):
        pygame.draw.rect(self.game_logic.gameDisplay, self.game_logic.saper_color, self.rect)
        pygame.draw.rect(self.game_logic.gameDisplay, self.game_logic.saper_head, self.head)

    def colission(self):
        for wall in self.game_logic.walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == 2:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if self.direction == 3:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if self.direction == 1:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if self.direction == 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                self.game_logic.chat.chat_log.append(text.Text("Twarda sciana.", self.game_logic.chat.saper_color))
                # if len(self.game_logic.chat.chat_log) > 10:
                # self.game_logic.chat.chat_log.pop(0)
                self.walk = False

    def move(self, meters):
        self.how = meters
        self.walk = True

    def walk(self):
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
        self.colission()

    def rotate(self):
        if self.direction == 0:
            self.direction = 2
        elif self.direction == 1:
            self.direction = 3
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 0
        self.walk = False

    def rotate_dir(self, direction):
        if direction == 'Lewo':
            self.direction = 3
            return True
        elif direction == 'Prawo':
            self.direction = 2
            return True
        elif direction == 'Dol':
            self.direction = 1
            return True
        elif direction == 'Przod':
            return True
        elif direction == 'Gora':
            self.direction = 0
            return True
        elif direction == 'Tyl':
            if self.direction == 1:
                self.direction = 0

            elif self.direction == 2:
                self.direction = 3

            elif self.direction == 0:
                self.direction = 1

            elif self.direction == 3:
                self.direction = 2

            return True
        return False

    def distance(self, game_object):
        return math.sqrt(pow(game_object.x / 32 - self.rect.x / 32, 2) + pow(game_object.y / 32 - self.rect.y / 32, 2))

    # (math.fabs(self.rect.x - self.game_logic.bomb.rect.x) / 32 < 8 and int(self.rect.y / 32) == int(
    # self.game_logic.bomb.rect.y / 32)) or (math.fabs(self.rect.y - self.game_logic.bomb.rect.y) / 32 < 8 and int(
    # self.rect.x / 32) == int( self.game_logic.bomb.rect.x / 32))

    def find_bomb(self):
        if 6 > self.distance(self.game_logic.bomb.rect) > 1 and not self.walk:
            self.to_find_bomb = False
            self.to_answer = True
            self.game_logic.chat.chat_log.append(
                text.Text("Zauwazylem bombe, podjechac do niej?", self.game_logic.chat.saper_color))

    def move_to_bomb(self):
        x1 = self.rect.x / 32
        x2 = self.game_logic.bomb.rect.x / 32
        y1 = self.rect.y / 32
        y2 = self.game_logic.bomb.rect.y / 32
        if self.distance(self.game_logic.bomb.rect) > 1:
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
            if self.game_logic.bomb.type == 1:
                self.game_logic.chat.chat_log.append(
                    text.Text("Podniesc ja, a moze rozbroic?", self.game_logic.chat.saper_color))
                self.answer1 = True
            elif self.game_logic.bomb.type == 2:
                self.game_logic.chat.chat_log.append(text.Text("Mam podniesc bombe?", self.game_logic.chat.saper_color))
                self.answer2 = True
            elif self.game_logic.bomb.type == 3:
                self.game_logic.chat.chat_log.append(text.Text("Sprobowac rozbroic?", self.game_logic.chat.saper_color))
                self.answer3 = True

    def pick_up(self):
        if self.distance(self.game_logic.bomb.rect) <= 1 and self.game_logic.bomb.lifting == True:
            self.bomb = True
            return True
        elif not self.bylo:
            if self.distance(self.game_logic.bomb.rect) > 1:
                self.game_logic.chat.chat_log.append(
                    text.Text("Nie mam tak dlugich raczek.", self.game_logic.chat.saper_color))
            elif not self.game_logic.bomb.lifting:
                self.game_logic.chat.chat_log.append(
                    text.Text("Nie moge podniesc tej bomby.", self.game_logic.chat.saper_color))
            self.bylo = True
        return False

    def drop(self):
        if self.bomb:
            self.bomb = False
            return True
        return False

    def Defuse(self, bomb):
        if (bomb.type == 1 or bomb.type == 3) and self.distance(self.game_logic.bomb.rect) <= 1:
            bomb.defused = True
        elif self.bylo == False and bomb.type == 2:
            self.game_logic.chat.chat_log.append(
                text.Text("Nie moge rozbroic tej bomby.", self.game_logic.chat.saper_color))
            self.bylo = True
        else:
            self.game_logic.chat.chat_log.append(text.Text("Musze byc blizej bomby.", self.game_logic.chat.saper_color))
            self.bylo = True

            # def Detonate(self, bomb):
