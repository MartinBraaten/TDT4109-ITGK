__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import math

#Alternerende sum

#   a) Skriv et program som leser heltallet n inn fra brukeren, og legger sammen tallserien 1^2-2^2+3^2-4^2...

n=int(input("Skriv inn et tall n: "))


sum=0
for i in range(1,1+n):
    sum+=((-1)**(i+1))*i**2
print(sum)


#   b) Skriv om programmet slik at det avslutter iterasjonen før summen av tallene er større enn n.
#   Hold styr på hvor mange ledd fra tallserien som er brukt i summen og skriv dette ut sammen med resultatet.


print()


p=int(input("Skriv inn hvor mange ledd du vil legge sammen i rekken 1^2 -2^2 + 3^2...+n^2: "))

sum=0
for i in range (1,p+1):
	z=((-1)**(i+1))*i**2
	if sum+z > p:
		break
	sum=sum+z
	ledd=i

print ("summen er",sum, "i leddet",ledd)
