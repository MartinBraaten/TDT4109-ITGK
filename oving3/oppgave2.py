__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Generelt om løkker

#  a) Lag en funksjon eller et program som summerer sammen tall fra 1 til 100.

sum = 0
for i in range(1,101):
    sum += i
    print("Summen er",sum)



#  b) Lag en funksjon eller et program som multipliserer sammen tallene fra 1,2,3,... og avslutter når produktet er større enn 1000.

print("b)")
x=1
n= 1000
produkt=1
while produkt<n:
    produkt*=x
    print(produkt)
    x+=1

#  c) Lag en funksjon eller et program som spør bruker det samme spørsmålet, om og om igjen, helt til det korrekte svaret blir skrevet.

svar=42
while True:
    tall2=int(input("Hva er svaret til alt i universet? \n"))
    if tall2==svar:
        print("du har svart rett")
        break
    else:
        print("Du har feil svar")
