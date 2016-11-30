#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def get_sentence_from_input_to_list():
    print "Witaj!"
    rozkaz = raw_input('Czekam na komende: ')
    podzielonyrozkaz = rozkaz.split()
    for i in range(len(podzielonyrozkaz)):
        sys.stdout.write(podzielonyrozkaz[i])
    return podzielonyrozkaz


def save_to_file(wordlist):
    words = open('../output/test.txt', 'w')
    for item in wordlist:
        words.write("%s\n" % item)
