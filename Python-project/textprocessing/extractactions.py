import sys


def getSentenceFromInputToList():
    print "Witaj!"
    rozkaz = raw_input('Czekam na komende: ')
    podzielonyrozkaz = rozkaz.split()
    for i in range(len(podzielonyrozkaz)):
        sys.stdout.write(podzielonyrozkaz[i])
    return podzielonyrozkaz


def saveToFile(string_list):
    file = open('test.txt', 'w')
    for item in string_list:
        file.write("%s\n" % item)
