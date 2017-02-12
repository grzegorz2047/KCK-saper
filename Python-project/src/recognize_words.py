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
    ACCEPTED = string.ascii_letters + string.digits + string.punctuation + "ęĘóĆśŚąĄżŻźŹćĆłŁÓ" + " "  # dodanie polskich znaków
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
        self.textpos.y = self.window.get_height() - (2 * self.text.get_height() + 6)

        self.fontobject = pygame.font.Font(None, 30)
        self.current_string = []
        self.zachecacz = " "
        self.command = ""

        self.chat_log = []
        self.user_color = (255, 255, 255)
        self.saper_color = (0, 0, 0)

        #do przetwarzania
        self.found_function = False
        self.found_object = False
        self.found_parametr = False
        self.found_number = False

        self.saved_function_name = ""
        self.saved_object_name = ""
        self.saved_number = 0
        self.saved_parameter_name = ""

        self.dont_understand = False
        self.actiondone = True;
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
        pygame.draw.rect(self.window, (122, 133, 144), [0, self.window.get_height() - 130 - 3 * 22, self.window.get_width(), 170], 0)
        pygame.draw.rect(self.window, (255, 255, 255), [0, self.window.get_height() - 130 - 3 * 22, self.window.get_width(), 170], 1)
        #render ramki czatu
        pygame.draw.rect(self.window, (122, 133, 144), [0, self.window.get_height() - 28, self.window.get_width(), 28], 0)
        pygame.draw.rect(self.window, (255, 255, 255), [0, self.window.get_height() - 28, self.window.get_width(), 28], 1)

        # render text
        self.window.blit(self.text, self.textpos)
        self.window.blit(self.fontobject.render("".join(self.current_string) + self.zachecacz, 1, (255, 255, 255)), (1, self.window.get_height() - 21))
        self.chat_log.reverse()
        for i in range(0, len(self.chat_log)):
            self.window.blit(self.fontobject.render("".join(self.chat_log[i].text), 1, self.chat_log[i].color), (1, self.window.get_height() - 50 - i * 18))
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
                if len(self.chat_log) > 9:
                    self.chat_log.pop(0)
                while len(self.current_string) != 0:
                    self.current_string.pop()

                #WYWOLUJE PRZETWARZANIE JEZYKA - Mikolaj
                self.przetwarzanie_jezyka();





    #PRZETWARZANIE JEZYKA - wywołanie. Mikolaj Balcerek
    #GLOWNA FUNKCJA do przetwarzania języka.
    def przetwarzanie_jezyka(self):
        self.actiondone = False;  # Parametr odpowiadający za sprawdzanie, czy dla pojedynczego rozkazu coś było zrozumiane i wykonane. Służy do odpowiedzi "Nie rozumiem".
        rozkazy = self.podziel_po_kropki(self.command) #Wywołanie funkcji dzielącej rozkaz po kropkach (Może zostać wykonane kilka rozkazów w ten sposób oddzielonych)
        self.found_number = False #Restartujemy stan przetwarzania dla każdego rozkazu oddzielonego kropką.
        self.saved_function_name = ""
        self.saved_object_name = ""
        self.saved_number = 0
        self.saved_parameter_name = ""
        for rozkaz in rozkazy: #pętla na podstawie ilości rozkazów po kropce
            words = self.get_sentence_from_input_to_list(rozkaz); #dzielimy pojedynczy rozkaz na slowa
            self.find_all(words); #wywołujemy przetwarzanie pojedynczych słów
            __main__.saper.Polecenia(); #Po znalezieniu i sklasyfikowaniu słów w pojedynczym rozkazie wywołujemy moduł rozmówek i sterowania saperem

    #Grzegorz Boiński
    def get_sentence_from_input_to_list(self, command):
        # rozkaz = raw_input('Czekam na komende: ')
        # podzielonyrozkaz = rozkaz.split()
        podzielonyrozkaz = command.split(" ")
        # for i in range(len(podzielonyrozkaz)):
        #     print (podzielonyrozkaz[i])
        return podzielonyrozkaz

    def podziel_po_kropki(self, command):
        podzielonyrozkaz = command.split(".")
        print podzielonyrozkaz;
        return podzielonyrozkaz


        #Funkcja klasyfikująca i rozróżniająca słowa rozkazu
        #Mikołaj Balcerek, Arek Powęska
    def find_all(self, words):
        for word in words:  #dla każdego słowa wykonujemy te operacje
            #Sprawdzamy, czy dane słowo należy do słownika podzielonego na trzy kategorie

            #FUNKCJA
            function_word = self.find_word(self.functions_file, word, 'funkcja') #W pliku Funkcje.xml szukamy obecnie przeglądanego słowa za pomocą funkcji find_word
            if function_word != "" and self.saved_function_name!="Zaprzeczenie": #jeżeli dane słowo zostało znalezione w Funkcje.xml i nie jest funkcją zaprzeczenia przechodzimy wewnątrz warunku
                self.found_function = True #znaleziono funkcje
                print "ZNALEZIONO FUNKCJE:"
                print function_word #nazwa typu funkcji znalezionej (np "Podnies")
                __main__.saper.bylo = False #funkcja nie została wykonana
                self.saved_function_name = function_word; #zapis nazwy znalezionej funkcji
                self.dont_understand = False #sprawdzanie, czy saper zrozumiał rozkaz
                continue
            else:
                self.dont_understand = True;


            #OBIEKT
            #Analogicznie jak dla funkcji, sprawdzamy czy słowo jest może obiektem
            object_word = self.find_word(self.objects_file, word, 'obiekt') #sprawdzamy czy słowo zawiera się w pliku Obiekty.xml
            if object_word != "":
                self.found_object = True #
                print "ZNALEZIONO OBIEKT:"
                print object_word;
                self.saved_object_name = object_word;
                self.dont_understand = False
                continue;

            #PARAMETR
            #sprawdzamy czy słowo/liczba spełnia warunki parametru
            parametr_word = self.find_word(self.parameters_file, word, 'parametr') #szukamy słowa w Parametry.xml
            #Poniżej znajduje się sprawdzanie, czy dane słowo nie jest przypadkiem liczbą arabską
            try:
                word = float(word); #konwersja słowa do typu float, wyjdzie z try jeżeli jest to string
                word = int(word);  # zaokrąglam części dziesiętne+
                self.found_number = True #znaleziono liczbę
                print "ZNALEZIONO LICZBĘ"
                print word;
                self.saved_number = word; #zapisano liczbę
                self.dont_understand = False
                continue; #przeskakujemy do obsługi kolejnego słowa rozkazu
            except ValueError: #słowo nie jest liczbą
                if parametr_word != "": #czy słowo zostało znalezione w pliku Parametry.xml?
                    self.found_parametr = True
                    print "ZNALEZIONO PARAMETR:"
                    print parametr_word
                    print word;
                    self.dont_understand = False
                    found_parameter = 1;
                    try: #SPRAWDZENIE CZY JEST LICZBĄ SŁOWNIE ZAPISANĄ - np. jeden, dwa
                        parametr_word = int(parametr_word); #funkcja wyszukiwania słów jest w stanie przekonwertować "jeden" w "1" (bo jeden to pisownia 1 zapisana w słowniku)
                        self.found_number = True; #należy jednak sprawdzić, czy "1" (string) jest liczbą)
                        self.saved_number = parametr_word; #zapisano liczbę
                    except ValueError:
                        self.saved_parameter_name = parametr_word; #okazany parametr nie jest liczbą zapisaną słownie, a zwykłym parametrem np. w górę
                    continue;



    #Mikołaj Balcerek
    #Funkcja szukająca danego słowa w słowniku XML. Wymaga podania nazwy pliku.
    def find_word(self, nazwaplikuxml, action, wordtype):
        root = nazwaplikuxml.getroot() #pobiera początek pliku-drzewa XML
        #w pętli będziemy przechodzić po pliku XML, przeglądając pola <spelling>
        #gdy znajdziemy słowo w polu <spelling>, zwracamy nazwę większego obiektu
        for block in root.findall(wordtype):  # iteruje po wszystkich obiektach
            for spelling in block.findall('spelling'):  # dla kazdej mozliwej odmiany slowa, alternatywnych pisowniach
                if spelling.text.lower() == action.lower():  # lower ignoruje duże/małe litery
                    return block.find('nazwa').text  # zwraca nazwę ogólnej kategorii szukanego słowa. Np dla "podniesiony" zwróci "Podnieś"
        return ""
