__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Navn


fornavn = ['johan', 'eli', 'mats', 'lene', 'simon', 'inger', 'henrik', 'mari', 'per']
etternavn = ['Hag', 'Hag', 'Basmestad', 'Grimlavaag', 'Kleivesund','Fintenes', 'Svalesand', 'Molteby', 'Hegesen']

#   a) Iterer forlengs gjennom de to listene, og skriv ut det fulle navnet på hver person.
"""
for fornavn, etternavn in zip(fornavn, etternavn):
	print(fornavn, etternavn)

#   b) Denne gangen gjør du nesten det samme, men itererer baklengs gjennom listen etternavn og forlengs gjennom fornavn.
#   Er noen av navnene like i forhold til forrige deloppgave? Hvorfor / hvorfor ikke?



print('Personene heter:')
etternavn.reverse()
for fornavn, etternavn in zip(fornavn, etternavn):
	print(fornavn, etternavn)


#   c) Du har sikkert merket at alle fornavnene mangler stor forbokstav. Endre programmet ditt til å skrive ut fornavnet med stor forbokstav for begge de forrige deloppgavene.
"""
from string import capwords
print('Personene heter:')
etternavn.reverse()
for fornavn, etternavn in zip(fornavn, etternavn):
	print(capwords(fornavn), etternavn)


