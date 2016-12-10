#!/usr/bin/env python
# -*- coding: utf-8 -*-
from extract_actions import *
from visualize_example import visualize
import xml.etree.cElementTree as ET


def main():

    #MIKOLAJ - Pokazuje jak korzystac ze Slownika dla Podnies Bombe na 2 metry
    #NIE DZIALA: Polskie znaki wgl (poradzi sobie ale zignoruje odpowiedz) (send help plz)
    #Zwraca z jakiegos powodu podwojnie
    #Zakładam, że zdanie zostało już oddzielone po kropce, i masz dostęp do pojedynczych wyrazów.
    wyrazjeden = "podniesiony"; #wyraz do sprawdzenia czy nalezy do jakies funkcji
    tablicawyrazow = [wyrazjeden];
    plik1 = ET.ElementTree(file='../Slownik/Funkcje.xml'); #odpalam plik funkcje i konwertuje na drzewo
    root = plik1.getroot() #poczatek drzewa

    for i in (0, len(tablicawyrazow) - 1):
        for funkcja in root.findall('funkcja'): #iteruje po wszystkich funkcjach
                for pisownie in funkcja.findall('spelling'): #dla kazdego mozliwego spelling (sprawdzam czy spelnia spelling)
                    if (pisownie.text == tablicawyrazow[i]):
                        print funkcja.find('nazwa').text; #wypisuje nazwe funkcji do wywolania
    #KONIEC MIKOŁAJ





    #save_to_file(get_sentence_from_input_to_list())
    visualize()








main()
