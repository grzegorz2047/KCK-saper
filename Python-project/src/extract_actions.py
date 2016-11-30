import sys

def getSentenceFromInputToList():
    print "Witaj!"
    rozkaz = raw_input('Czekam na komende: ')
    podzielonyrozkaz = rozkaz.split()
    for i in range(len(podzielonyrozkaz)):
        sys.stdout.write(podzielonyrozkaz[i])
    return podzielonyrozkaz

def saveToFile(list):
    file = open('../output/test.txt', 'w')
    for item in list:
        file.write("%s\n" % item)
