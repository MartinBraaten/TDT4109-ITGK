__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

def r(n):

    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*r(n-1)
print(r(n=int(input("Skriv inn et tall: "))))

liste=[1,2,3,[4,5],6,7,[2,3,[5,3]],8,9,10]
def list(liste):
    tot=0
    for element in liste:
        if type(element)==type([]):
            tot+=list(element)
        else:
            tot+=element
    return tot

print(list(liste))

def readfromfile(filename):
    file=open(filename,"r")
    size=int(file.readline())
    board=[]