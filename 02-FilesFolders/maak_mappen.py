import os

bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:

    tekst_regel = tekst_regel.strip()
    os.mkdir(tekst_regel)

    tekst_regel = bestand.readline()
