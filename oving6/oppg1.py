__author__ = 'Martinskole'
# -*- coding: utf-8 -*-


#   Teori

"""
a) Hvordan representerer datamaskiner tegn?

med bits?

b) Hvor mange bits trenger man får å representere et dobbeltpresisjonstall? Hvor mange bytes? Hva er det minste desimaltallet (i absoluttverdi) som kan bli representert?

64, 8, 16 desimaltall

c) Hva er 18 i totallssystemet? Hva er 18 i 16 tallssystemet?

10010, 12

d) Skriv OLE ved hjelp av ASCII.

OLE= 01001111 01001100 01000101

e) Hva er en piksel, og hva er dens funksjon i datamaskinens sammenheng?

pixler er små punkter av farget lys. ved å variere farge og intensitet kan hvilken som helst farge bli dannet på skjermen.

f) Hva er forskjellen på analog og digital lyd? Hvordan kan vi gå fra den ene til den andre?

Analog lyd er vanlig kontinuerlig lyd. Digital lyd er analog lyd omgjort til bits. Lyden blir tatt opp av en mikrofon, og gjort om til elektriske bølger.
Signalet går så inn i en ADC (analog-to-digital converter), som tar å sampler med bestemte intervaller. De binære tallene blir så lagret i minnet.

g) Hva er metadata?

Metadata er informasjon som beskriver data.

"""

#   Generelt om lister

#   a) Lag en liste li med alle heltallene fra 1 til og med 6.
#   b) Gang alle oddetallene i li med -1. Sørg for at endringen blir lagret i listen.
#   c) Sorter listen omvendt (dvs. høyest til lavest) ved hjelp av pythonlisters innebygde sorteringsmetode.
#   d) Skriv listen ut til skjermen.

Li=[1,2,3,4,5,6]

def odd():
    for i in range(len(Li)):
        if not i%2==0:
            Li.pop(len(Li)-(i+1))
            Li.append(-1*i)

odd()

Li.sort()
print(Li)
