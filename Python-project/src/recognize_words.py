#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pygame
import string
import sys
import extract_actions
reload(sys)
sys.setdefaultencoding('utf8')
import text
import __main__

class Chat:
    ACCEPTED = string.ascii_letters + string.digits + string.punctuation + "ęĘóĆśŚąĄżŻźŹćĆłŁÓ" + " "  # bedzie trzeba pokombinowac
    ACCEPTED = ACCEPTED.decode("utf-8")
    def __init__(self, screen):
        #ladowanie czcionki
        self.font = pygame.font.SysFont("monospace", 15)

        # okno gry :)
        self.window = screen

        #czy czat jest aktywny
        self.active = True
        self.unicode = False

        #zegarek
        self.time_start = pygame.time.get_ticks()
        self.time_current = 0

        self.functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')
        self.objects_file = ET.ElementTree(file='../Slownik/Obiekty.xml')
        self.parameters_file = ET.ElementTree(file='../Slownik/Parametry.xml')

        self.text = self.font.render("CHAT", 1, (255, 255, 255))
        self.textpos = self.text.get_rect()
        self.textpos.x = self.window.get_width() / 2 - self.text.get_width() / 2
        self.textpos.y = self.window.get_height() - (2 * self.text.get_height() + 5)

        self.fontobject = pygame.font.Font(None, 18)
        self.current_string = []
        self.zachecacz = " "
        self.command = ""

        self.chat_log = []
        self.user_color = (255, 255, 255)
        self.saper_color = (255, 20, 20)

        #do przetwarzania
        self.found_function = False
        self.found_object = False
        self.found_parametr = False
        self.found_number = False

        self.saved_function_name = ""
        self.saved_object_name = ""
        self.saved_number = 0
        self.saved_parameter_name = ""
        pass

    def Update(self):
        if self.active == True:
            self.time_current = (pygame.time.get_ticks() - self.time_start) / 1000

            if self.time_current > 0.5:
                self.time_start = pygame.time.get_ticks()
                self.zachecacz = "|"
            else:
                self.zachecacz = " "

    def Render(self):
        #render historia czatu
        pygame.draw.rect(self.window, (122, 133, 144), [0, self.window.get_height() - 22 - 3 * 22, self.window.get_width(), 64], 0)
        pygame.draw.rect(self.window, (255, 255, 255), [0, self.window.get_height() - 24 - 3 * 22, self.window.get_width(), 68], 1)
        #render ramki czatu
        pygame.draw.rect(self.window, (122, 133, 144), [0, self.window.get_height() - 22, self.window.get_width(), 20], 0)
        pygame.draw.rect(self.window, (255, 255, 255), [0, self.window.get_height() - 24, self.window.get_width(), 24], 1)

        # render text
        self.window.blit(self.text, self.textpos)
        self.window.blit(self.fontobject.render("".join(self.current_string) + self.zachecacz, 1, (255, 255, 255)), (1, self.window.get_height() - 21))
        self.chat_log.reverse()
        for i in range(0, len(self.chat_log)):
            self.window.blit(self.fontobject.render("".join(self.chat_log[i].text), 1, self.chat_log[i].color), (1, self.window.get_height() - 41 - i * 13))
        self.chat_log.reverse()


    def get_key(self, event_key):
            if event_key.unicode in self.ACCEPTED:
                self.unicode = True
                return event_key.unicode
            else:
                return event_key.key

    def ask(self, event_key):
            inkey = self.get_key(event_key)
            length = len(self.current_string)
            remove = False
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
                    #self.chat_log.append("".join(self.current_string))
                    self.chat_log.append(text.Text("".join(self.current_string), self.user_color))
                if len(self.chat_log) > 4:
                    self.chat_log.pop(0)
                while len(self.current_string) != 0:
                    self.current_string.pop()

                #WYWOLUJE PRZETWARZANIE JEZYKA - Mikolaj
                self.przetwarzanie_jezyka();





    #PRZETWARZANIE JEZYKA - Mikolaj

    #GLOWNA FUNKCJA, TO WYWOLUJEMY RECZNIE TYLKO
    def przetwarzanie_jezyka(self):
        words = self.get_sentence_from_input_to_list(self.command);
        self.find_all(words);


    def get_sentence_from_input_to_list(self, command):
        # rozkaz = raw_input('Czekam na komende: ')
        # podzielonyrozkaz = rozkaz.split()
        podzielonyrozkaz = command.split(" ")
        # for i in range(len(podzielonyrozkaz)):
        #     print (podzielonyrozkaz[i])
        return podzielonyrozkaz



    def find_all(self, words):
        #PRZETWARZANIE JEZYKA main part
        #Znajdzie funkcje, parametr, obiekt w dowolnej kolejnosi. Nie potrafi jeszcze powiedziec, czy akurat ta funkcja pasuje do tego parametru/obiektu.
        found_function = 0;
        found_object = 0;
        found_parameter = 0;
        for word in words:

            #FUNKCJA
            function_word = self.find_word(self.functions_file, word, 'funkcja')
            if function_word != "":
                self.found_function = True #
                print "ZNALEZIONO FUNKCJE:"
                print function_word
                __main__.saper.bylo = False
                self.found_number = False
                self.saved_function_name = ""
                self.saved_object_name = ""
                self.saved_number = 0
                self.saved_parameter_name = ""
                self.saved_function_name = function_word;
                found_function = 1;
                #words.remove(word)
                continue

            #OBIEKT
            object_word = self.find_word(self.objects_file, word, 'obiekt')
            if object_word != "":
                self.found_object = True #
                print "ZNALEZIONO OBIEKT:"
                print object_word;
                self.saved_object_name = object_word;
                found_object = 1;
                continue;

            #parametr
            parametr_word = self.find_word(self.parameters_file, word, 'parametr')
            # SPRAWDZAM CZY NIE JEST LICZBĄ, NIE USUWAJCIE
            try:
                word = float(word);
                word = int(word);  # zaokrąglam części dziesiętne+
                self.found_number = True
                print "ZNALEZIONO LICZBĘ"
                print word;
                found_parameter = 1;
                self.saved_number = word;
                continue;
            except ValueError:
                if parametr_word != "":
                    self.found_parametr = True
                    print "ZNALEZIONO PARAMETR:"
                    print parametr_word
                    print word;
                    found_parameter = 1;
                    self.saved_parameter_name = parametr_word;
                    continue;
        




    def find_word(self, nazwaplikuxml, action, wordtype):
        root = nazwaplikuxml.getroot()

        for block in root.findall(wordtype):  # iteruje po wszystkich obiektach
            for spelling in block.findall('spelling'):  # dla kazdej mozliwej odmiany
                if spelling.text.lower() == action.lower():  # lower by ignorowały duże/małe litery
                    return block.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
        return ""