__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
"""
for i in range(10):
    print(i)

print(range(10))




liste=[3, 2, 2, 13, 37]
sum=0
for tall in liste:
    sum += tall
print(sum)


for x in range(0,21):
    if x%2==0:
        print(x)

"""
""""
sum = 0
while True:
    tall=int(input("Skriv inn et tall: \n"))
    if tall==-1:
        break
    sum += tall
    print("Summer er",sum)

"""
"""
sum = 0
while sum<100:
    tall=int(input("Skriv inn et tall: \n"))
    if tall==-1:
        break
    sum += tall
    print("Summer er",sum)
"""


"""
import random
liste=[]
for i in range(10):
    liste.append(random.randint(2,20))
print(liste)
"""
"""


x=int(input("Skriv inn tall 1: \n"))
y=int(input("Skriv inn tall 2: \n"))


def divisible(x,y):
    if x%y==0:
        print(x,"er delelig på",y)
    else:
        print(x,"er ikke delelig på",y)
divisible(x,y)
"""


def liste_delelig(liste,divisor):
    for tall in liste:
        if tall % divisor==0
            delelige_tall+=1
            print(delelige_tall +=1)
