#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue

from extract_actions import *
from visualize_example import get_command
import xml.etree.cElementTree as ET
import pygame
import string
import __main__


class Chat:
    ACCEPTED = string.ascii_letters + string.digits + string.punctuation + "ęĘóĆśŚąĄżŻźŹćĆłŁ" + " "  # bedzie trzeba pokombinowac
    ACCEPTED = ACCEPTED.decode("utf-8")
    def __init__(self):
        self.active = False
        self.functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')
        self.objects_file = ET.ElementTree(file='../Slownik/Obiekty.xml')
        self.parameters_file = ET.ElementTree(file='../Slownik/Parametry.xml')
        pass

    # funkcja obiekt parametr

    def Update(self):
        self.get_key()


    def find_all(self, words):
        for word in words:
            function_word = find_word(self.functions_file, word, 'funkcja')
            if function_word != "":
                print function_word
                words.remove(word)
            for word in words:
                object_word = find_word(self.functions_file, word, 'obiekt')
                if object_word != "":
                    print object_word
                    words.remove(word)
                for word in words:
                    try:
                        word += 1
                        print word
                        words.remove(word)
                    except TypeError:
                        print word
                        words.remove(word)

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.unicode in self.ACCEPTED:
                    return event.unicode
                else:
                    return event.key

    def ask(screen, question):
        "ask(screen, question) -> answer"
        pygame.font.init()
        current_string = []
        display_box(screen, question + ": " + string.join(current_string, ""))
        while 1:
            inkey = get_key()
            if inkey == K_BACKSPACE:
                current_string = current_string[0:-1]
            elif inkey == K_RETURN:
                break
            elif inkey == K_MINUS:
                current_string.append("_")
            elif inkey == K_SPACE:
                current_string.append(" ")
            else:
                current_string.append(inkey)
            display_box(screen, question + ": " + string.join(current_string, ""))
        return string.join(current_string, "")

    def display_box(screen, message):
        "Print a message in a box in the middle of the screen"
        fontobject = pygame.font.Font(None, 18)
        pygame.draw.rect(screen, (0, 0, 0),
                         ((screen.get_width() / 2) - 100,
                          (screen.get_height() / 2) - 10,
                          200, 20), 0)
        pygame.draw.rect(screen, (255, 255, 255),
                         ((screen.get_width() / 2) - 102,
                          (screen.get_height() / 2) - 12,
                          204, 24), 1)
        if len(message) != 0:
            screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                        ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
        pygame.display.flip()

    def find_word(xmlfile, action, wordtype):
        root = xmlfile.getroot()

        for block in root.findall(wordtype):  # iteruje po wszystkich objektach
            for spelling in block.findall('spelling'):  # dla kazdej mozliwej odmiany
                if spelling.text.lower() == action.lower():  # lower by ignorowały duże/małe litery
                    return block.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
        return ""


    # def main():
    #     queue = Queue()
    #     command = get_command()
    #     words = get_sentence_from_input_to_list(command)
    #     chat = Chat()
    #     chat.find_all(words)
    #
    # main()
