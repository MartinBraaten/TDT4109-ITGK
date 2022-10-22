__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Valuta kalkyle

print("Tast 1 for ja og 2 for nei")
Ja= 1
Nei= 2

euro=8.7                #verdi for valutaene nå
GBP=11.9
RUB=0.14

seuro=9.1                #verdi for valutaene senere
sGBP=12.1
sRUB=0.15


BP=0.05                #prosent for bank
FLP=0.1                #prosent for flyplass



bankeuronå= euro+euro*BP
bankGBPnå= GBP+GBP*BP
bankRUBnå= RUB+RUB*BP

flyplasseuronå= euro+euro*FLP
flyplassGBPnå= GBP+GBP*FLP
flyplassRUBnå= RUB+RUB*FLP

bankeurosenere= seuro+seuro*BP
bankGBPsenere= sGBP+sGBP*BP
bankRUBsenere= sRUB+sRUB*BP                                    #diverse utregninger

flyplasseurosenere= seuro+seuro*FLP
flyplassGBPsenere= sGBP+sGBP*FLP
flyplassRUBsenere= sRUB+sRUB*FLP

valuta=input("Hvilken valuta vil du veksle til?: ")
nå=input("Vil du veksle pengene nå?: ")                           #spørsmål til bruker
bank=input("Vil du veksle pengene i en bank?: ")

if valuta=="euro":
    if nå=="ja":
        if bank=="ja":
            print("Du får",bankeuronå,"av den valutaen per krone")
        elif bank==Nei:
            print("Du får",flyplasseuronå,"av den valutaen per krone")
    elif nå==Nei:
        if bank==Ja:
            print("Du får",bankeurosenere,"av den valutaen per krone")
        elif bank==Nei:
            print("Du får",flyplasseurosenere,"av den valutaen per krone")
elif valuta==GBP:
    if nå==Ja:
        if bank==Ja:
            print("Du får",bankGBPnå,"av den valutaen per krone")
        elif bank==Nei:
            print("Du får",flyplassGBPnå,"av den valutaen per krone")
    elif nå==Nei:
        if bank==Ja:
            print("Du får",bankGBPsenere,"av den valutaen per krone")
        elif bank==Nei:
            print("Du får",flyplassGBPsenere,"av den valutaen per krone")
elif valuta==RUB:
    if nå==Ja:
        if bank==Ja:
            print("Du får",bankRUBnå,"av den valutaen per krone")
        elif bank==Nei:
            print("Du får",flyplassRUBnå,"av den valutaen per krone")
    elif nå==Nei:
        if bank==Ja:
            print("Du får",bankRUBsenere,"av den valutaen per krone")
        elif bank==Nei:
            print("Du får",flyplassRUBsenere,"av den valutaen per krone")

