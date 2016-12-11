#!/usr/bin/env python
# -*- coding: utf-8 -*-
from extract_actions import *
from visualize_example import get_command
import xml.etree.cElementTree as ET


def find_function(action):
    # MIKOLAJ - Pokazuje jak korzystac ze Slownika dla Podnies Bombe na 2 metry
    # NIE DZIALA: Polskie znaki wgl (poradzi sobie ale zignoruje odpowiedz) (send help plz)
    # Zwraca z jakiegos powodu podwojnie
    # Zakładam, że zdanie zostało już oddzielone po kropce, i masz dostęp do pojedynczych wyrazów.
    functions_file = ET.ElementTree(file='../Slownik/Funkcje.xml')  # odpalam plik funkcje i konwertuje na drzewo
    root = functions_file.getroot()  # poczatek drzewa

    for funkcja in root.findall('funkcja'):  # iteruje po wszystkich funkcjach
        for pisownie in funkcja.findall('spelling'):  # dla kazdej mozliwej odmiany
            if pisownie.text == action:
                return funkcja.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
    return ""
    # KONIEC MIKOŁAJ


def main():
    command = get_command()
    words = get_sentence_from_input_to_list(command)
    for word in words:
        function = find_function(word)
        if find_function(word) != "":
            print function

            # save_to_file(get_sentence_from_input_to_list())
            # visualize()


main()
