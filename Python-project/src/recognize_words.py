#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pygame
import string
import linecache

class Chat:
    ACCEPTED = string.ascii_letters + string.digits + string.punctuation + "ęĘóĆśŚąĄżŻźŹćĆłŁ" + " "  # bedzie trzeba pokombinowac
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

    def get_key(self, event_key):
            if event_key.unicode in self.ACCEPTED:
                self.unicode = True
                return event_key.unicode
            else:
                return event_key.key

    def ask(self, event_key):
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
                #self.chat_log.append(linecache.getline("chat_log.txt", len(self.chat_log)))
                print(self.chat_log)
                while len(self.current_string) != 0:
                    self.current_string.pop()

    # def find_all(self, words):
    #     for word in words:
    #         function_word = self.find_word(self.functions_file, word, 'funkcja')
    #         if function_word != "":
    #             print function_word
    #             words.remove(word)
    #         for word in words:
    #             object_word = self.find_word(self.functions_file, word, 'obiekt')
    #             if object_word != "":
    #                 print object_word
    #                 words.remove(word)
    #             for word in words:
    #                 try:
    #                     word += 1
    #                     print word
    #                     words.remove(word)
    #                 except TypeError:
    #                     print word
    #                     words.remove(word)
    #
    # def find_word(xmlfile, action, wordtype):
    #     root = xmlfile.getroot()
    #
    #     for block in root.findall(wordtype):  # iteruje po wszystkich objektach
    #         for spelling in block.findall('spelling'):  # dla kazdej mozliwej odmiany
    #             if spelling.text.lower() == action.lower():  # lower by ignorowały duże/małe litery
    #                 return block.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
    #     return ""