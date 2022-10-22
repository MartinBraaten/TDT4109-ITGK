__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

"""

#Teorioppgave2

a) Hva er pseudokode og når får vi bruk for det? Lag en pseudokode for steking av speilegg.

En pseudokode er en slags algoritme som er ment for mennesker og ikke datamaskiner. Det kan være nyttig for å forklare ting til andre.
Knekk egget i to
    Ikke ødelegg plommen
Stek ved lav varme
    Avslutt når når hviten har stivnet


b) Hva er et flytdiagram?

Et flytdiagram er et diagram som viser steg et program tar. det er 3 typer symbol, oval, paralellogram og rektangel.
Ovalen er start og slutt, paralellogram blir brukt som input og output symboler, og rektangler er brukt som prosesseringssymbol.

c) Hva er debugging?

Det er å rette opp feil i koden.

d) Hva er forskjellen på et høynivå- og et lavnivå-programmeringsspråk?

i et lavnivå-programmeringsspråk må man skrive mye mer kode og samtidig vite hvordan CPUen kommuniserer med output enhetene.
 høynivå bruker mer tekst og er lettere å forstå, og trenger ikke vite noe om CPUen.

e) Forklar de fem stegene i Hente/Utføre-kretsen.

1. Hente instruksjonen som er i minnet
2. dekode instruksjonen
3. Operand dataen hentes fra munnet
4. subtrakjssjon operasjonen blir utført på verdiene
5. resultatet blir sendt tibake til minnet


f) Hva gjør programtelleren (Program Counter)?

programtelleren holder orden på adressen til instruksjonen til et program, så programmet blir utført kronologisk.

"""

#Fibonacci

#   a) Lag et program som regner ut og returnerer det k-te fibonaccitallet f(k) ved hjelp av iterasjon.
#   b) Skriv om programmet i deloppgave a) slik at det også regner ut summen av alle fibonaccitallene.


a = 0
b = 1
t=1
k = int(input('Skriv inn hvor mange fibonaccitall du vil ha:'))
def f():
    global a,b
    b = a + b
    a = b - a
    print(b)


if k == 1:
    print(0)
    print("Summen er 0")
elif k == 2:
    print(0)
    print(1)
    print("Summen er 1")
else:
    print(0)
    print(1)
    for i in range(k-2):
        f()
        t +=b
    print("summen er",t)



