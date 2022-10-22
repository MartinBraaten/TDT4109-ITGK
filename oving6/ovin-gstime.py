__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

Liste=[1,2,3,4,5]
print(Liste)


Liste.reverse()
print(Liste)



for i in range(2,10):
    if not i % 2==0:
        Liste.append(i)
print(Liste)


print(len(Liste))
Liste.sort(reverse=True)
print(Liste)


def maybeappend(liste,tall):
    templiste=liste
    if tall not in templiste:
        templiste.append(tall)
    return templiste


Liste.pop(len(Liste)-1)
Liste.append(5)
print(Liste)


variabel=Liste.index(4)
Liste.insert(0,variabel)
print(Liste)


def partall(liste):
    antall =0
    for i in liste:
        if i % 2 ==0:
            antall +=1
    print("Antall partall er", antall)
partall(Liste)


def find_duplicates(liste):
    outList=[]
    for tall in liste:
        if liste.count(tall)>=2:
            outList=maybeappend(outList,tall)
    return outList
print(find_duplicates(Liste))

