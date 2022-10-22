__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#   strenghåndetring



#   a) Lag en funksjon som sjekker om to strenger er like ved å sammenligne dem tegn for tegn. Funksjonen returnerer True hvis strengene er like; False ellers.

def likellerulik(x,y):
    o = []
    p = []
    while x:
        o.append(x[:1])
        x = x[1:]
    while y:
        p.append(y[:1])
        y = y[1:]
    if len(o)==len(p):
        for i in range(len(o)):
            if o[i]!=p[i]:
                print("Tekstene er ulik")
                break
            else:
                print("Tekstene er lik")

    else:
        print("Tekstene er ulik")

likellerulik(x=input("Skriv inn en tekst her: "),y=input("Skriv inn en tekst her: "))



#   b) Lag en funksjon som tar inn en streng, reverserer den og returnerer den reverserte strengen. Dette skal gjøres tegn for tegn med en løkke.

def reversere(tekst):
    asd = []
    while tekst:
        asd.append(tekst[:1])
        tekst = tekst[1:]
    asd.reverse()
    print(asd)


reversere(tekst=input("Skriv inn en tekst som skal reverseres: "))

#   c) Et palindrom er et ord som staves likt begge veier (eks. “abba”). Lag en funksjon som returnerer True om en streng er et palindrom; False ellers.

def palindrom(streng):
    rstreng=[]
    asdstreng=[]
    while streng:
        rstreng.append(streng[:1])
        asdstreng.append(streng[:1])
        streng = streng[1:]
    rstreng.reverse()
    for i in range(len(rstreng)):
        if rstreng[i]!=asdstreng[i]:
            print("Tekstene er ulik")
            break
        else:
            print("Tekstene er lik")
palindrom(streng=input("skriv inn en tekst for å sjekke palindrom: "))



#   d) Lag en funksjon som tar inn to strenger og sjekker om den første strengen inneholder den andre. Dersom den gjør det, returner posisjonen den andre strengen begynner på (fra 0). Returner False ellers.

def inneholder(tekst1,tekst2):
    if tekst2 in tekst1:
        print("Tekst2 er på index-plass nr ",tekst1.find(tekst2),"i tekst1")
    else:
        print("False")



inneholder(tekst1=input("Skriv inn tekst1: "), tekst2=input("Skriv inn tekst2: "))