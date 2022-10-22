__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#   Arbeidsdager
#   b) Lag funksjonen is_workday(weekday) som tar inn en ukedag, og returnerer True om ukedagen er arbeidsdag, og False ellers.

d=-1
dag=['mandag','tirsdag','onsdag','torsdag','fredag','lørdag','søndag']
def is_workday():
    if dag[d % 7]=='lørdag' or dag[d % 7]=='søndag':
        return False
    else:
        return True

#   c) Lag funksjonen workdays_in_year(year) som tar inn et årstall og skriver ut antall arbeidsdager i det gitte året.
#    Husk at skuddår har et en ekstra dag i februar. Skriv ut antall arbeidsdager for årene 1900 til og med 1919.
"""
def workdays_in_year():
    if
"""
#   a) Lag en funksjonen weekday_newyear som tar inn et årstall, og returnerer hvilken ukedag året starter på.
#   Ukedager representeres med heltall, dvs. mandag = 0, tirsdag = 1, ..., søndag = 6.

print("År | Ukedag| Arbeidsdag | Antall arbeidsdager i året:")
a=1899
def ukedag():
    global a,d
    if a%100==0:
        d+=1
    elif a%4==0:
        d+=2
    else:
        d+=1
    a+=1

    print(a, dag[d % 7], is_workday())
for i in range (20):
    ukedag()
    is_workday()
  #  workdays_in_year()



