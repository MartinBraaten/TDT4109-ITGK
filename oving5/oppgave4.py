__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Kollektiv-app

def bilettpris(alder):
    if alder<5:
        print("Biletten er gratis")
    elif alder>=5 and alder<=20:
        print("Biletten koster 20kr")
    elif alder>=21 and alder<=25:
        print("Biletten koster 50kr")
    elif alder>=26 and alder<=60:
        print("Biletten koster 80kr")
    else:
        print("Biletten er gratis")

bilettpris(alder=int(input("Skriv inn din alder: ")))



