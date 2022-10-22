__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Karatergrenser

x=float(input("Skriv inn antall poeng: "))
if x != round(x):
    print("du har tastet feil")

elif x<0 or x>100:
    print("Du har tastet inn feil")
elif x>88 and x<=100:
    print("Karakter A")
elif x<89 and x>76:
    print("Karakter B")
elif x<77 and x>64:
    print("Karakter C")
elif x<65 and x>52:
    print("Karakter D")
elif x<53 and x>40:
    print("Karakter E")
elif x>-1 and x<41:
    print("Karakter F")
