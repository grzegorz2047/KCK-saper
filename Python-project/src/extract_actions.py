#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_sentence_from_input_to_list(command):
    # rozkaz = raw_input('Czekam na komende: ')
    # podzielonyrozkaz = rozkaz.split()
    podzielonyrozkaz = command.split(" ")
    # for i in range(len(podzielonyrozkaz)):
    #     print (podzielonyrozkaz[i])
    return podzielonyrozkaz


def save_to_file(wordlist):
    words = open('../output/test.txt', 'w')
    for item in wordlist:
        words.write("%s\n" % item)
