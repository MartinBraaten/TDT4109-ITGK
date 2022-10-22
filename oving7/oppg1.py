__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#løkker og lister


#a)
numbers=[1,3,5,8,12,4,2,7,9,3,7]

def seperate(numbers,threshold):
    utliste=[]
    yololiste=[]
    for tall in numbers:
        if tall <= threshold:
            utliste.append(tall)
        else:
            yololiste.append(tall)
    print(utliste, yololiste)
seperate(numbers, threshold=int(input("Skriv inn et tall for threshold: ")))


def seperate5(numbers,threshold):
    utliste=[]
    yololiste=[]
    for tall in numbers:
        if tall <= threshold:
            utliste.append(tall)
    return utliste


#b)

liste=[1,2,3,4,5,6,7,8,9,10]

def  multiplication_table(n):
    templist=seperate5(liste,n)
    s=n
    drit=[]
    asd=[]
    while True:
        if s>0:
            drit.append(s)
            s=s-1
        else:
            break
    drit.sort()

    for tall in templist:
        y=tall
        for mordi in drit:
            asd.append(mordi*y)
    print(asd)



multiplication_table(n=int(input("Skriv inn en verdi for tallet n: ")))