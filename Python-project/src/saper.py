import pygame
import __main__
import text
import math


class Saper(object):
    def __init__(self, game_logic_arg, bomb_arg, chat_arg, game_display_arg):
        # lokalizacja_startowa
        self.game_display = game_display_arg
        self.chat = chat_arg
        self.bomb_obj = bomb_arg
        self.game_logic = game_logic_arg
        self.saper_x = 1
        self.saper_y = 1

        # szerokosc o dlugosc sapera
        self.saper_width = 32
        self.saper_height = 32

        # kierunek {"North" : 0, "South" : 1, "East" : 2, "West" : 3}
        self.direction = 0

        self.walking = False

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

    def update(self, wall):
        if self.to_find_bomb:
            self.find_bomb()
        if self.answer:
            self.move_to_bomb()
        if self.walking:
            self.walk(wall)
        if self.bomb:
            self.bomb_obj.rect.x = self.rect.x + self.bomb_obj.bomb_width / 2
            self.bomb_obj.rect.y = self.rect.y + self.bomb_obj.bomb_height / 2
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
            if self.chat.saved_function_name == "Zaprzeczenie":
                self.chat.chat_log.append(text.Text("Ok.", self.chat.saper_color))
                self.chat.saved_function_name = ""
                self.to_answer = False

            if self.chat.saved_function_name == "Zgoda":
                self.chat.chat_log.append(text.Text("Jade do niej.", self.chat.saper_color))
                self.chat.saved_function_name = ""
                self.to_answer = False
                self.answer = True
        elif self.answer1:
            if self.chat.saved_function_name == "Podnies":
                self.pick_up()
                self.answer1 = False
                self.chat.chat_log.append(text.Text("Ale ciezka.", self.chat.saper_color))
                self.chat.saved_function_name = ""
            elif self.chat.saved_function_name == "Rozbroj":
                self.Defuse(self.bomb_obj)
                self.answer1 = False
                self.chat.chat_log.append(text.Text("Sie robi.", self.chat.saper_color))
                self.chat.saved_function_name = ""
            elif self.chat.saved_function_name == "Zaprzeczenie":
                self.answer1 = False
                self.chat.chat_log.append(text.Text("Nie to nie.", self.chat.saper_color))
                self.chat.saved_function_name = ""
        elif self.answer2:
            if self.chat.saved_function_name == "Podnies" or self.chat.saved_function_name == "Zgoda":
                self.pick_up()
                self.answer2 = False
                self.chat.chat_log.append(text.Text("Gotowe.", self.chat.saper_color))
                self.chat.saved_function_name = ""
        elif self.answer3:
            if self.chat.saved_function_name == "Rozbroj" or self.chat.saved_function_name == "Zgoda":
                self.Defuse(self.bomb_obj)
                self.answer3 = False
                self.chat.chat_log.append(text.Text("Uff, zyje!", self.chat.saper_color))
                self.chat.saved_function_name = ""
        elif self.chat.saved_function_name == "Zaprzeczenie":
            self.chat.saved_function_name = ""
            self.chat.saved_parameter_name = ""
            self.chat.saved_number = 0
            self.chat.found_number = False
            self.chat.chat_log.append(
                text.Text("Nie wykonam rozkazu poprzedzonego zaprzeczeniem", self.chat.saper_color))
        elif self.chat.saved_function_name == "Pojedz" and self.walking == False and self.chat.found_number == True:
            self.rotate_dir(self.chat.saved_parameter_name)
            self.move(self.chat.saved_number)
            self.chat.saved_function_name = ""
            self.chat.saved_parameter_name = ""
            self.chat.saved_number = 0
            self.chat.found_number = False
        elif self.chat.saved_function_name == "Pojedz" and self.bylo == False and self.walking == False:
            self.chat.chat_log.append(
                text.Text("O ile kratek mam sie przemiescic?", self.chat.saper_color))
            self.bylo = True

        elif self.chat.saved_function_name == "Podnies" and self.chat.saved_object_name == "Bomba" and self.pick_up():
            self.chat.chat_log.append(text.Text("Podnioslem.", self.chat.saper_color))
            self.chat.saved_function_name = ""
            self.chat.saved_object_name = ""

        elif self.chat.saved_function_name == "Podnies" and self.bylo == False:
            self.chat.chat_log.append(
                text.Text("Nie wiem co mam podniesc.", self.chat.saper_color))
            self.bylo = True

        elif self.chat.saved_function_name == "Obroc":
            if self.rotate_dir(self.chat.saved_parameter_name):
                self.chat.chat_log.append(text.Text("Obrocilem sie.", self.chat.saper_color))
                self.chat.saved_function_name = ""
                self.chat.saved_parameter_name = ""
            elif not self.bylo:
                self.chat.chat_log.append(
                    text.Text("W ktora strone mam sie obrocic?", self.chat.saper_color))
                self.bylo = True

        elif self.chat.saved_function_name == "Upusc":
            if self.drop():
                self.chat.chat_log.append(text.Text("Gotowe.", self.chat.saper_color))
                self.chat.saved_function_name = ""
            elif not self.bylo:
                self.bylo = True
                self.chat.chat_log.append(text.Text("Nie mam co upuscic.", self.chat.saper_color))

        elif self.chat.saved_function_name == "Rozbroj" and self.chat.saved_object_name == "Bomba":
            self.Defuse(self.bomb_obj)
            self.chat.chat_log.append(text.Text("Rozborilem.", self.chat.saper_color))
            self.chat.saved_function_name = ""
            self.chat.saved_object_name = ""
        elif self.chat.saved_function_name == "Rozbroj" and self.bylo == False:
            self.chat.chat_log.append(
                text.Text("Nie wiem co mam rozbroic.", self.chat.saper_color))
            self.bylo = True
        elif self.chat.dont_understand:
            self.chat.chat_log.append(text.Text("Nie rozumiem.", self.chat.saper_color))
            self.chat.dont_understand = False

        while len(self.chat.chat_log) > 9:
            self.chat.chat_log.pop(0)
            # ##############################################################################################################3

    def render(self):
        pygame.draw.rect(self.game_display, self.game_logic.colors.saper_color, self.rect)
        pygame.draw.rect(self.game_display, self.game_logic.colors.saper_head, self.head)

    def colission(self, wall):
        for wall in wall.walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == 2:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if self.direction == 3:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if self.direction == 1:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if self.direction == 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                self.chat.chat_log.append(text.Text("Twarda sciana.", self.chat.saper_color))
                # if len(self.chat.chat_log) > 10:
                # self.chat.chat_log.pop(0)
                self.walking = False

    def move(self, meters):
        self.how = meters
        self.walking = True

    def walk(self, wall):
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
                self.walking = False
            self.how -= 1
        else:
            self.walking = False
        self.colission(wall)

    def rotate(self):
        if self.direction == 0:
            self.direction = 2
        elif self.direction == 1:
            self.direction = 3
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 0
        self.walking = False

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

    # (math.fabs(self.rect.x - self.bomb_obj.rect.x) / 32 < 8 and int(self.rect.y / 32) == int(
    # self.bomb_obj.rect.y / 32)) or (math.fabs(self.rect.y - self.bomb_obj.rect.y) / 32 < 8 and int(
    # self.rect.x / 32) == int( self.bomb_obj.rect.x / 32))

    def find_bomb(self):
        if 6 > self.distance(self.bomb_obj.rect) > 1 and not self.walking:
            self.to_find_bomb = False
            self.to_answer = True
            self.chat.chat_log.append(
                text.Text("Zauwazylem bombe, podjechac do niej?", self.chat.saper_color))

    def move_to_bomb(self):
        x1 = self.rect.x / 32
        x2 = self.bomb_obj.rect.x / 32
        y1 = self.rect.y / 32
        y2 = self.bomb_obj.rect.y / 32
        if self.distance(self.bomb_obj.rect) > 1:
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
            if self.bomb_obj.type == 1:
                self.chat.chat_log.append(
                    text.Text("Podniesc ja, a moze rozbroic?", self.chat.saper_color))
                self.answer1 = True
            elif self.bomb_obj.type == 2:
                self.chat.chat_log.append(text.Text("Mam podniesc bombe?", self.chat.saper_color))
                self.answer2 = True
            elif self.bomb_obj.type == 3:
                self.chat.chat_log.append(text.Text("Sprobowac rozbroic?", self.chat.saper_color))
                self.answer3 = True

    def pick_up(self):
        if self.distance(self.bomb_obj.rect) <= 1 and self.bomb_obj.lifting == True:
            self.bomb = True
            return True
        elif not self.bylo:
            if self.distance(self.bomb_obj.rect) > 1:
                self.chat.chat_log.append(
                    text.Text("Nie mam tak dlugich raczek.", self.chat.saper_color))
            elif not self.bomb_obj.lifting:
                self.chat.chat_log.append(
                    text.Text("Nie moge podniesc tej bomby.", self.chat.saper_color))
            self.bylo = True
        return False

    def drop(self):
        if self.bomb:
            self.bomb = False
            return True
        return False

    def Defuse(self, bomb):
        if (bomb.type == 1 or bomb.type == 3) and self.distance(self.bomb_obj.rect) <= 1:
            bomb.defused = True
        elif self.bylo == False and bomb.type == 2:
            self.chat.chat_log.append(
                text.Text("Nie moge rozbroic tej bomby.", self.chat.saper_color))
            self.bylo = True
        else:
            self.chat.chat_log.append(text.Text("Musze byc blizej bomby.", self.chat.saper_color))
            self.bylo = True

            # def Detonate(self, bomb):
