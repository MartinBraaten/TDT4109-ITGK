__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import math


h = float(10**-3)
x = float(3.14)
f1 = (math.sin(x))
f2 = (math.sin(x+h))
derivative = (f2-f1)/h
print(derivative)


h = float(input("Skriv inn en verdi for h: "))
x = float(input("Skriv inn en verdi for x: "))
f1 = (math.sin(x))
f2 = (math.sin(x+h))
derivative = (f2-f1)/h
print(derivative)
