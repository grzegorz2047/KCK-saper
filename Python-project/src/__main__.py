#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue

from extract_actions import *
from visualize_example import get_command
import xml.etree.cElementTree as ET


class Function:
    def __init__(self, function_name):
        self.function_name = function_name


def find_function(action):
    # MIKOLAJ - Pokazuje jak korzystac ze Slownika dla Podnies Bombe na 2 metry
    # NIE DZIALA: Polskie znaki wgl (poradzi sobie ale zignoruje odpowiedz) (send help plz)
    # Zwraca z jakiegos powodu podwojnie
    # Zakładam, że zdanie zostało już oddzielone po kropce, i masz dostęp do pojedynczych wyrazów.
    functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')  # odpalam plik funkcje i konwertuje na drzewo
    root = functions_file.getroot()  # poczatek drzewa

    for function_string in root.findall('funkcja'):  # iteruje po wszystkich funkcjach
        for spelling in function_string.findall('spelling'):  # dla kazdej mozliwej odmiany
            if spelling.text == action:
                return Function(function_string.find('nazwa').text)  # wypisuje nazwe funkcji do wywolania
    return Function("")
    # KONIEC MIKOŁAJ


def main():
    queue = Queue()
    command = get_command()
    words = get_sentence_from_input_to_list(command)
    for word in words:
        function = find_function(word)
        if find_function(word).function_name != "":
            print function.function_name

            # save_to_file(get_sentence_from_input_to_list())
            # visualize()


main()
