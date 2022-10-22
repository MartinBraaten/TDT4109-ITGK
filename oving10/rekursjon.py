__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

# a) Lag en rekursiv funksjon som regner ut summen av 1+2+...n, hvor n er et parameter til funksjonen.
def rekt(n):
    if n==1:
        return 1
    else:
        return n+rekt(n-1)
print(rekt(n=int(input("Skriv inn et heltall: "))))

print()
# b) Lag en rekursiv funksjon som finner det minste elementet i en liste.
liste=[5,6,7,8,3,54,6,11,3,2,15,6,8,12,1,-5]
def minst(liste):
    for i in range(0,len(liste)-1):
        if liste==sorted(liste):
            return liste[0]
        elif liste[i]>liste[i+1]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
            return minst(liste)


print("Det minste elementet i listen er:", minst(liste))

#c) Regn ut sin(x) rekursivt ved å benytte at sin(x)=3sin(x/3)−4sin3(x/3) og at sin(x)=x når x er mye mindre enn 1.
#Hint: Du skal ikke bruke den innebygde sinus-funksjonen.
def asd(x):
    if x<0.001:
        return x
    else:
        return 3*asd(x/3)-4*(asd(x/3))**3


print(asd(x=float(input("Skriv inn en verdi for x: "))))


