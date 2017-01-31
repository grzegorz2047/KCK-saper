#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
import string
import sys
import text
import __main__

reload(sys)
sys.setdefaultencoding('utf8')


class Output:
    custom = False
    custom_msg = ""
    function_name = ""
    object_name = ""
    parameter_name = ""
    saved_number = 0

    found_function = False
    found_object = False
    found_parametr = False
    found_number = False

    def __init__(self):
        pass


class Chat:
    ACCEPTED = string.ascii_letters + string.digits + string.punctuation + "ęĘóĆśŚąĄżŻźŹćĆłŁÓ" + " "  # bedzie trzeba pokombinowac
    ACCEPTED = ACCEPTED.decode("utf-8")

    def __init__(self, screen):
        # ladowanie czcionki
        self.font = pygame.font.SysFont("monospace", 15)

        # okno gry :)
        self.window = screen

        # czy czat jest aktywny
        self.active = True
        self.unicode = False

        # zegarek
        self.time_start = pygame.time.get_ticks()
        self.time_current = 0

        self.text = self.font.render("CHAT", 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.x = self.window.get_width() / 2 - self.text.get_width() / 2
        self.textpos.y = self.window.get_height() - (2 * self.text.get_height() + 6)

        self.fontobject = pygame.font.Font(None, 30)
        self.current_string = []
        self.command_prompt = " "
        self.command = ""

        self.chat_log = []
        self.user_color = (255, 255, 255)
        self.saper_color = (0, 0, 0)
        pass

    def update(self):
        if self.active:
            self.time_current = (pygame.time.get_ticks() - self.time_start) / 1000

            if self.time_current > 0.5:
                self.time_start = pygame.time.get_ticks()
                self.command_prompt = "|"
            else:
                self.command_prompt = " "

    def render(self):
        # render historia czatu
        pygame.draw.rect(self.window, (122, 133, 144),
                         [0, self.window.get_height() - 130 - 3 * 22, self.window.get_width(), 170], 0)
        pygame.draw.rect(self.window, (255, 255, 255),
                         [0, self.window.get_height() - 130 - 3 * 22, self.window.get_width(), 170], 1)
        # render ramki czatu
        pygame.draw.rect(self.window, (122, 133, 144), [0, self.window.get_height() - 28, self.window.get_width(), 28],
                         0)
        pygame.draw.rect(self.window, (255, 255, 255), [0, self.window.get_height() - 28, self.window.get_width(), 28],
                         1)

        # render text
        self.window.blit(self.text, self.textpos)
        self.window.blit(self.fontobject.render("".join(self.current_string) + self.command_prompt, 1, (255, 255, 255)),
                         (1, self.window.get_height() - 21))
        self.chat_log.reverse()
        for i in range(0, len(self.chat_log)):
            self.window.blit(self.fontobject.render("".join(self.chat_log[i].text), 1, self.chat_log[i].color),
                             (1, self.window.get_height() - 50 - i * 18))
        self.chat_log.reverse()

    def get_key(self, event_key):
        if event_key.unicode in self.ACCEPTED:
            self.unicode = True
            return event_key.unicode
        else:
            return event_key.key

    def ask(self, event_key, saper, file_controller):
        inkey = self.get_key(event_key)
        length = len(self.current_string)
        if inkey == pygame.K_BACKSPACE and length != 0:
            self.current_string.pop()
        elif inkey == pygame.K_MINUS:
            self.current_string.append("_")
        elif inkey == pygame.K_SPACE:
            self.current_string.append(" ")
        elif self.unicode:
            self.unicode = False
            self.current_string.append(inkey)
        elif inkey == pygame.K_RETURN:
            self.command = "".join(self.current_string)
            plik = open('chat_log.txt', 'a')
            self.current_string.append("\n")
            plik.writelines(self.current_string)
            plik.close()
            self.current_string.pop()
            if "".join(self.current_string) != "":
                # self.chat_log.append("".join(self.current_string))
                self.chat_log.append(text.Text("".join(self.current_string), self.user_color))
            if len(self.chat_log) > 9:
                self.chat_log.pop(0)
            while len(self.current_string) != 0:
                self.current_string.pop()

            # WYWOLUJE PRZETWARZANIE JEZYKA - Mikolaj
            self.przetwarzanie_jezyka(saper, file_controller, self.command)

    # PRZETWARZANIE JEZYKA - Mikolaj

    # GLOWNA FUNKCJA, TO WYWOLUJEMY RECZNIE TYLKO
    def przetwarzanie_jezyka(self, saper, file_controller, command):
        rozkazy = self.podziel_po_kropki(command)
        for rozkaz in rozkazy:
            words = self.get_sentence_from_input_to_list(rozkaz)
            output = self.find_all(words, saper, file_controller)
            saper.polecenia(output)

    def get_sentence_from_input_to_list(self, command):
        # rozkaz = raw_input('Czekam na komende: ')
        # podzielonyrozkaz = rozkaz.split()
        podzielonyrozkaz = command.split(" ")
        # for i in range(len(podzielonyrozkaz)):
        #     print (podzielonyrozkaz[i])
        return podzielonyrozkaz

    def podziel_po_kropki(self, command):
        podzielonyrozkaz = command.split(".")
        print podzielonyrozkaz
        return podzielonyrozkaz

    def find_all(self, words, saper, file_controller):
        # PRZETWARZANIE JEZYKA main part
        output = Output()
        for word in words:

            # FUNKCJA
            function_word = self.find_word(file_controller.functions_file, word, 'funkcja')
            if function_word != "" and output.function_name != "Zaprzeczenie":
                output.found_function = True  #
                print "ZNALEZIONO FUNKCJE:"
                print function_word
                saper.bylo = False
                output.function_name = function_word
                self.dont_understand = False
                continue
            else:
                self.dont_understand = True

            # OBIEKT
            object_word = self.find_word(file_controller.objects_file, word, 'obiekt')
            if object_word != "":
                output.found_object = True  #
                print "ZNALEZIONO OBIEKT:"
                print object_word
                output.saved_object_name = object_word
                self.dont_understand = False
                continue

            # parametr
            parametr_word = self.find_word(file_controller.parameters_file, word, 'parametr')
            # SPRAWDZAM CZY NIE JEST LICZBĄ, NIE USUWAJCIE
            try:
                word = float(word);
                word = int(word);  # zaokrąglam części dziesiętne+
                output.found_number = True
                print "ZNALEZIONO LICZBĘ"
                print word
                output.saved_number = word
                self.dont_understand = False
                continue
            except ValueError:
                if parametr_word != "":
                    output.found_parametr = True
                    print "ZNALEZIONO PARAMETR:"
                    print parametr_word
                    print word
                    self.dont_understand = False
                    found_parameter = 1
                    try:  # SPRAWDZENIE CZY JEST LICZBĄ SŁOWNIE ZAPISANĄ
                        output.parametr_word = int(parametr_word)
                        output.found_number = True
                        output.saved_number = parametr_word
                    except ValueError:
                        output.parameter_name = parametr_word
                    continue
        return output

    def find_word(self, nazwaplikuxml, action, wordtype):
        root = nazwaplikuxml.getroot()

        for block in root.findall(wordtype):  # iteruje po wszystkich obiektach
            for spelling in block.findall('spelling'):  # dla kazdej mozliwej odmiany
                if spelling.text.lower() == action.lower():  # lower by ignorowały duże/małe litery
                    return block.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
        return ""
