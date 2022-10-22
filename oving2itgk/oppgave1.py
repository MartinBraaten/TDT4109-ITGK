__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import math


"""
#Teorioppgave
a) Hva er forskjellen på primær og sekundær lagring? Nevn eksempler på disse.

Pimærlagring foregår i f.eks i RAMen. Der blir det lagret midlertidig. Lagring i HDD eller SSD er permanent og er eksempler på sekundærlagring. USB, CD og DVD er også sekundærlagring.

b)Harddisk, SSD og RAM: Nevn de ulike egenskapene med tanke på permanent/volatilt og tilfeldig/sekvensiell aksess.

RAM er volatilt, som betyr at når pcen skrus av, vil all data forsvinne. I en permantent lagringsplass som ssd, vil det ikke bli slettet.
RAM står for "random-access memory", fordi CPUen kan nå data som er lagret tilfeldig i RAMmen, og det skjer ganske raskt.
Det skjer raskere enn sekvensiell aksess.

c)Silisium brukes mye i elektronikk. Hvorfor?

Silisium er veldig vanlig stoff. Det kan manipuleres til å lede strøm noen ganger, men andre ganger ikke. Dette utnttes i en pc mtp å sende signaler.

d) Hvordan kan en datamaskin lagre og behandle bilder, lyd og tekst?

Bildene, lyden og teksten blir konvertert til binærkode, og lagret. Man kan så senere manipulere binærkoden som man vil.

e) Det overføres 32 000 bytes mellom to datamaskiner. Hva må netthastigheten (målt i bits) være for å fullføre denne overføringen i løpet av 40 sekunder?

(32 000 * 8)/40 = 6400 bits per sekund

f) Hva er et OS og hva brukes det til?

OS står for operativsystem, og er en programvare som tildeler forskjellige ressurser til andre programmer i datamaskinen.
Det er operativsystemet som holder styr på komponentene som er i pcen og koblet til pcen, og gir andre programmer tilgang til dem.

"""






#Andregradsligning

a = int(input("Skriv inn en verdi for a: "))
b = int(input("Skriv inn en verdi for b: "))
c = int(input("Skriv inn en verdi for c: "))

d=b*b-4*a*c



if d < 0:
    print('Ligningen har to imaginære røtter.')
elif d > 0:
    print('Ligningen har to reelle røtter.')
else:
    print('Ligningen har en reel rot.')













