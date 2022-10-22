__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

# Forenkling av brøker
b_ny=0
def f(a,b):
    while b!=0:
        b_ny=b
        b_ny+=a%b
        a=b
    return a
    print(a,b)


f(a=int(input("Skriv inn en verdi for a: ")),b=int(input("Skriv inn en verdi for b: ")))
