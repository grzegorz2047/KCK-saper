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

class Function:
    def __init__(self, function_name):
        self.function_name = function_name

class Object:
    def __init__(self, object_name):
        self.object_name = object_name

class Parameter:
    def __init__(self, parameter_name):
        self.parameter_name = parameter_name

def find_function(action):
    # MIKOLAJ - Pokazuje jak korzystac ze Slownika: szukanie słowa w funkcjach
    # Zakładam, że zdanie zostało już oddzielone po kropce, jest dostęp do pojedynczych wyrazów.
    functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')  #ścieżka do pliku
    root = functions_file.getroot()  # poczatek drzewa

    for function_string in root.findall('funkcja'):  # iteruje po wszystkich funkcjach
        for spelling in function_string.findall('spelling'):  # dla kazdej mozliwej odmiany
            if spelling.text.lower() == action.lower(): # lower by ignorowały duże/małe litery
                return Function(function_string.find('nazwa').text)  # wypisuje nazwe funkcji do wywolania
    return Function("")

def find_object(action):
    objects_file = ET.ElementTree(file='../Slownik/Obiekty.xml')  #ścieżka do pliku
    root = objects_file.getroot()

    for object_string in root.findall('obiekt'):  # iteruje po wszystkich objektach
        for spelling in object_string.findall('spelling'):  # dla kazdej mozliwej odmiany
            if spelling.text.lower() == action.lower(): # lower by ignorowały duże/małe litery
                return Object(object_string.find('nazwa').text)  # wypisuje nazwe objektu do wywolania
    return Object("")

def find_parameter(action):
    parameters_file = ET.ElementTree(file='../Slownik/Parametry.xml')
    root = parameters_file.getroot()  # poczatek drzewa

    for parameter_string in root.findall('parametr'):  # iteruje po wszystkich objektach
        for spelling in parameter_string.findall('spelling'):  # dla kazdej mozliwej odmiany
            if spelling.text.lower() == action.lower(): # lower by ignorowały duże/małe litery
                return Parameter(parameter_string.find('nazwa').text)  # wypisuje nazwe objektu do wywolania
    return Parameter("")

def main():
    queue = Queue()
    command = get_command()
    words = get_sentence_from_input_to_list(command)
    for word in words:
        function = find_function(word)
        if find_function(word).function_name != "":
            print function.function_name
            words.remove(word)
        for word in words:
            object = find_object(word)
            if find_object(word).object_name != "":
                print object.object_name

            # save_to_file(get_sentence_from_input_to_list())
            # visualize()

    # if function.function_name == "Podnies":
    #     object = find_object(word)
    #     parameter = find_parameter(word)
    #     if find_object(word).object_name != "" and find_parameter(word).parameter_name != "":
    #         print (function.function_name , "(" , object.object_name , "," , parameter.parameter_name , ")")
    #
    # elif function.function_name == "Zdetonuj":
    #     object = find_object(word)
    #     parameter = find_parameter(word)
    #     if find_object(word).object_name != "" and find_parameter(word).parameter_name != "":
    #         print (function.function_name, "(", object.object_name, ")")
    #
    # elif function.function_name == "Pojedz":
    #     parameter = find_parameter(word)
    #     if find_parameter(word).parameter_name != "":
    #         print (function.function_name, "(", parameter.parameter_name, ")")

main()

