#!/usr/bin/env python
# -*- coding: utf-8 -*-
from extract_actions import *
from visualize_example import getCommand
import xml.etree.cElementTree as ET


def findFunction(action):
    # MIKOLAJ - Pokazuje jak korzystac ze Slownika dla Podnies Bombe na 2 metry
    # NIE DZIALA: Polskie znaki wgl (poradzi sobie ale zignoruje odpowiedz) (send help plz)
    # Zwraca z jakiegos powodu podwojnie
    # Zakładam, że zdanie zostało już oddzielone po kropce, i masz dostęp do pojedynczych wyrazów.
    tablicawyrazow = [action];
    plik1 = ET.ElementTree(file='../Slownik/Funkcje.xml')  # odpalam plik funkcje i konwertuje na drzewo
    root = plik1.getroot()  # poczatek drzewa

    for i in (0, len(tablicawyrazow) - 1):
        for funkcja in root.findall('funkcja'):  # iteruje po wszystkich funkcjach
            for pisownie in funkcja.findall(
                    'spelling'):  # dla kazdego mozliwego spelling (sprawdzam czy spelnia spelling)
                if pisownie.text == tablicawyrazow[i]:
                    return funkcja.find('nazwa').text  # wypisuje nazwe funkcji do wywolania
    return ""
    # KONIEC MIKOŁAJ


def main():
    command = getCommand()
    words = get_sentence_from_input_to_list(command)
    for word in words:
        function = findFunction(word)
        if findFunction(word) != "":
            print function

            # save_to_file(get_sentence_from_input_to_list())
            # visualize()


main()
