__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Tempraturkonverterer

f=int(input("Skriv inn temperaturen i fahrenheit: "))
c=format((f-32)/1.8, '.2f')
print("Dette tilsvarer",c,"grader celsius.")
