#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue

from extract_actions import *
from visualize_example import get_command
import xml.etree.cElementTree as ET
import pygame
import map
import saper
import bomb


class Chat:
    def __init__(self):
        self.functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')
        self.objects_file = ET.ElementTree(file='../Slownik/Obiekty.xml')
        self.parameters_file = ET.ElementTree(file='../Slownik/Parametry.xml')
        pass

    # funkcja obiekt parametr

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


def find_word(xmlfile, action, wordtype):
    root = xmlfile.getroot()

    for block in root.findall(wordtype):  # iteruje po wszystkich objektach
        for spelling in block.findall('spelling'):  # dla kazdej mozliwej odmiany
            if spelling.text.lower() == action.lower():  # lower by ignorowały duże/małe litery
                return block.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
    return ""


def main():
    queue = Queue()
    command = get_command()
    words = get_sentence_from_input_to_list(command)
    chat = Chat()
    chat.find_all(words)

main()
