__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#   mynter


liste = [20,1,5,10,10,10,20,5]

def countcoins(liste):
    tyve=0
    ti=0
    fem=0
    en=0
    while True:
        for tall in liste:
            if tall==20:
                tyve+=1
            elif tall==10:
                ti+=1
            elif tall==5:
                fem+=1
            elif tall==1:
                en+=1
        break
    print([tyve,ti,fem,en])
countcoins(liste)


Liste = [12,23,34,45,56,67,78,89,90,98,87,65,54,43,21]
def numcoins(Liste):
        nyListe=[]
        vektliste=[]
        tjuere=0
        tiere=0
        femmere=0
        enere=0
        for tall in Liste:
            temptall=tall
            tempListe=Liste
            while temptall!=0:
                if temptall>=20:
                    tjuere+=1
                    temptall-=20
                elif temptall>=10:
                    tiere+=1
                    temptall-=10
                elif temptall>=5:
                    femmere+=1
                    temptall-=5
                elif temptall>=1:
                    enere+=1
                    temptall-=1
            vekt=9.9*tjuere+6.8*tiere+7.85*femmere+4.35*enere
            nyListe.append([tjuere,tiere,femmere,enere])
            vektliste.append([vekt])
            tjuere=0
            tiere=0
            femmere=0
            enere=0
        print(nyListe)
        print(vektliste)

numcoins(Liste)

