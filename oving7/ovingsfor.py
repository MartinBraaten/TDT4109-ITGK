__author__ = 'Martinskole'
# -*- coding: utf-8 -*-



print(ord("a"))
print(chr(122))

def difference(a,b):
    tall1=ord(a)
    tall2=ord(b)
    avstand = abs(tall1-tall2)
    return min(avstand,26-avstand)
print(difference("a","f"))


__author__ = 'Kristoffer'
# -*- coding: utf-8 -*-
import random

# Returnerer et kast
def startKast():
    mitt_kast = []
    for i in range(5):
        mitt_kast.append(random.randint(1,6))
    return mitt_kast

#Sjekker en hånd for antall av et bestemt tall
def sjekk(hand, tall):
    antall = 0
    for i in hand:
        if i==tall:
            antall += 1
    return  antall

#Sjekker en hånd for par og returnerer poeng
def like(hand,antall):
    if sjekk(hand,6)>=antall:
        return 6*antall
    if sjekk(hand,5)>=antall:
        return 5*antall
    if sjekk(hand,4)>=antall:
        return 4*antall
    if sjekk(hand,3)>=antall:
        return 3*antall
    if sjekk(hand,2)>=antall:
        return 2*antall
    if sjekk(hand,1)>=antall:
        return 1*antall
    return 0

# triller en terning i en bestemt posisjon på ny
def nyTerning(liste,posisjon):
    utListe = liste
    utListe[posisjon] = random.randint(1,6)
    return utListe

# Sjekker om spilleren får bonus eller ikke
####################################################################################### Oppgave 2.5


# henter en liste over hvilke terninger som skal triller på ny (indeksen) (1-indeksert)
####################################################################################### Oppgave 2.4
def nytt_kast_indexer():
    text = input("Hvile terninger vil du kaste på ny? (separer med komma uten mellomrom (1-indexert) \n")
    if not text:
        return []
    indekser = text.split(",")
    utListe = []
    for i in indekser:
        utListe.append(int(i)-1) #NB: endrer tilbake til 0-index
    return utListe

# alle terningene som ligger på indeksene trilles på ny
def nytt_kast(innListe,indekser):
    utListe = innListe
    for i in indekser:
        utListe = nyTerning(utListe,i)
    return utListe


# alternativ liste for å trille terninger på ny, bruker verdien i stedet for posisjonen
####################################################################################### Oppgave 2.4
def nytt_kast_value_indexer(kast):
    text = input("Hvilke terninger vil du kaste på ny? (skriv inn verdien til terningene) \n")
    if not text:
        return []
    indekser = text.split(",")
    utListe = []
    for i in indekser:
        utListe.append(int(i))
    return change_value_to_index(kast,utListe)

# helping function to return the right index of a die-number
def findIndexer(list, number, tolerance):
    index = -1
    for i in range(len(list)):
        if list[i]==number:
            if tolerance == 0:
                return i
            else:
                tolerance -= 1
    return -1

# changes from face-value of die to array position
def change_value_to_index(kast,values):
    tolerance = [0,0,0,0,0,0]
    indexes = []
    values.sort()
    for i in range(len(values)):
        target = values[i]
        index = findIndexer(kast,target,tolerance[target-1])
        tolerance[target-1] += 1
        indexes.append(index)
    return indexes


# kaster terningene tre ganger og spør om rerolls mellom hver gang
############################################################################################## Oppgave 2.2
#Lag en funksjon fullfører alle tre kastene og som spør hva som skal kastes på ny etter kast en og to
#
#	kast = [] , print() , verdier = nytt_kast_indexer() ,
#	mitt_kast = nytt_kast(mitt_kast,verdier)
#
def kast():
    #første kast
    mitt_kast = startKast()
    print(mitt_kast)

    #andre kast
    verdier = nytt_kast_indexer()
    #verdier = nytt_kast_value_indexer(mitt_kast)
    mitt_kast = nytt_kast(mitt_kast,verdier)
    print(mitt_kast)

    #tredje kast
    verdier = nytt_kast_indexer()
    #verdier = nytt_kast_value_indexer(mitt_kast)
    mitt_kast = nytt_kast(mitt_kast,verdier)
    print(mitt_kast)
    return mitt_kast

# brukes for i øverste del av yatzy spillet
def faseEn(kast,verdi):
    poeng = 0
    antall = sjekk(kast,verdi)
    poeng += verdi * antall
    print("\nDu fikk",poeng,"poeng får å ha",antall,"av",verdi)
    return poeng

# gir poeng for to par
############################################################################################# Oppgave 2.6
def toPar(hand):
    etPar = like(hand,2)
    if etPar > 0:
        verdi = etPar/2
        hand.pop(hand.index(verdi))
        hand.pop(hand.index(verdi))
        andrePar = like(hand,2)
    if etPar and andrePar and (etPar is not andrePar):
        return etPar+andrePar
    return 0

############################################################################################ Oppgave 2.8
# gir poeng for straight

# gir poeng for liten straight

# gir poeng for stor straight




############################################################################################ Oppgave 2.3
# Skriv en main funksjon som går gjennom de seks første kastene og printer poengene til slutt
# mitt_kast = kast() , poeng += faseEn(mitt_kast, x)
def main():
    poeng = 0

############################################################################################ Oppgave 2.7
# Et par, tre like, to par
main()


__author__ = 'Kristoffer'
# -*- coding: utf-8 -*-
import random
#http://codeshare.io/dV1xE

# Returnerer et kast
def startKast():
    mitt_kast = []
    for i in range(5):
        mitt_kast.append(random.randint(1,6))
    return mitt_kast

#Sjekker en hånd for antall av et bestemt tall
def sjekk(hand, tall):
    antall = 0
    for i in hand:
        if i==tall:
            antall += 1
    return  antall

#Sjekker en hånd for par og returnerer poeng
def like(hand,antall):
    if sjekk(hand,6)>=antall:
        return 6*antall
    if sjekk(hand,5)>=antall:
        return 5*antall
    if sjekk(hand,4)>=antall:
        return 4*antall
    if sjekk(hand,3)>=antall:
        return 3*antall
    if sjekk(hand,2)>=antall:
        return 2*antall
    if sjekk(hand,1)>=antall:
        return 1*antall
    return 0

# triller en terning i en bestemt posisjon på ny
def nyTerning(liste,posisjon):
    utListe = liste
    utListe[posisjon] = random.randint(1,6)
    return utListe

# Sjekker om spilleren får bonus eller ikke
####################################################################################### Oppgave 2.5


# henter en liste over hvilke terninger som skal triller på ny (indeksen) (1-indeksert)
####################################################################################### Oppgave 2.4
def nytt_kast_indexer():
    text = input("Hvile terninger vil du kaste på ny? (separer med komma uten mellomrom (1-indexert) \n")
    if not text:
        return []
    if text == "alle":
        return [0,1,2,3,4]
    indekser = text.split(",")
    utListe = []
    for i in indekser:
        utListe.append(int(i)-1) #NB: endrer tilbake til 0-index
    return utListe

# alle terningene som ligger på indeksene trilles på ny
def nytt_kast(innListe,indekser):
    utListe = innListe
    for i in indekser:
        utListe = nyTerning(utListe,i)
    return utListe


# alternativ liste for å trille terninger på ny, bruker verdien i stedet for posisjonen
####################################################################################### Oppgave 2.4
def nytt_kast_value_indexer(kast):
    text = input("Hvilke terninger vil du kaste på ny? (skriv inn verdien til terningene) \n")
    if not text:
        return []
    indekser = text.split(",")
    utListe = []
    for i in indekser:
        utListe.append(int(i))
    return change_value_to_index(kast,utListe)

# helping function to return the right index of a die-number
def findIndexer(list, number, tolerance):
    index = -1
    for i in range(len(list)):
        if list[i]==number:
            if tolerance == 0:
                return i
            else:
                tolerance -= 1
    return -1

# changes from face-value of die to array position
def change_value_to_index(kast,values):
    tolerance = [0,0,0,0,0,0]
    indexes = []
    values.sort()
    for i in range(len(values)):
        target = values[i]
        index = findIndexer(kast,target,tolerance[target-1])
        tolerance[target-1] += 1
        indexes.append(index)
    return indexes


# kaster terningene tre ganger og spør om rerolls mellom hver gang
############################################################################################## Oppgave 2.2
#Lag en funksjon fullfører alle tre kastene og som spør hva som skal kastes på ny etter kast en og to
#
#	kast = [] , print() , verdier = nytt_kast_indexer() ,
#	mitt_kast = nytt_kast(mitt_kast,verdier)
#
def kast():
    #første kast
    mitt_kast = startKast()
    print(mitt_kast)

    #andre kast
    verdier = nytt_kast_indexer()
    #verdier = nytt_kast_value_indexer(mitt_kast)
    mitt_kast = nytt_kast(mitt_kast,verdier)
    print(mitt_kast)

    #tredje kast
    verdier = nytt_kast_indexer()
    #verdier = nytt_kast_value_indexer(mitt_kast)
    mitt_kast = nytt_kast(mitt_kast,verdier)
    print(mitt_kast)
    return mitt_kast

# brukes for i øverste del av yatzy spillet
def faseEn(kast,verdi):
    poeng = 0
    antall = sjekk(kast,verdi)
    poeng += verdi * antall
    print("\nDu fikk",poeng,"poeng får å ha",antall,"av",verdi)
    return poeng

# gir poeng for to par
############################################################################################# Oppgave 2.6
def toPar(hand):
    etPar = like(hand,2)
    if etPar > 0:
        verdi = etPar/2
        hand.pop(hand.index(verdi))
        hand.pop(hand.index(verdi))
        andrePar = like(hand,2)
    if etPar and andrePar and (etPar is not andrePar):
        return etPar+andrePar
    return 0

############################################################################################ Oppgave 2.8
# gir poeng for straight

# gir poeng for liten straight

# gir poeng for stor straight




############################################################################################ Oppgave 2.3
# Skriv en main funksjon som går gjennom de seks første kastene og printer poengene til slutt
# mitt_kast = kast() , poeng += faseEn(mitt_kast, x)
def main():
    poeng = 0
    for i in range(1,7):
        mitt_kast = kast()
        poeng += faseEn(mitt_kast,i)
    print("Du fikk",poeng,"poeng for de seks første kastene")
############################################################################################ Oppgave 2.7
# Et par, tre like, to par
main()

