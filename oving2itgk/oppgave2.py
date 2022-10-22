__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import math
import random


#Generelt om betingelser

a = int(input("Skriv inn en verdi for a: "))
b = int(input("Skriv inn en verdi for b: "))

x=a*b
y=a+b
if x<y:
    print("a*b er mindre enn a+b")
elif x>y:
    print("a*b er større enn a+b")
else:
    print("a*b=a+b")

print("")
z = int(input("Hva er 3*4? Skriv svaret ditt her: "))
if z<12 or z>12:
    print("Du har svart feil, svaret er 12")
elif z==12:
    print("Du har svart korrekt")

