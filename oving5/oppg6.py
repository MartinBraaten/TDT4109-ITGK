__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#multiplikasjon
z=0
a=0
k=0
while True:
    tol=0.0001
    k+=1
    z+=1
    x=((1+1/k**2))
    sum=x**z
    if tol>x:
        break
    a+=1               #teller antall iterasjoner


print (x)
print(sum)
print("Det trengs",(a),"iterasjoner.")

