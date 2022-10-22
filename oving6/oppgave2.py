__author__ = 'Martinskole'
# -*- coding: utf-8 -*-
import math
#   Vektorer


def main():
	vec1 = getVector()
	vec1_lengde = getLengde(vec1)
	print("vec1 = ",vec1,", og lengden til den første vektoren er: ",vec1_lengde,sep='')

	skalar = getSkalar()
	vec2 = skalarMult(vec1,skalar)

	vec2_lengde = getLengde(vec2)
	print("Lengden til den andre vektoren er: ",vec2_lengde,sep='')

	finnForskjell(vec1_lengde,vec2_lengde)

	vec3 = getVector()
	produkt = indreProdukt(vec1,vec3)

	print("Indreproduktet av vec1 og vec3 er: ",produkt,sep='')

def getVector():
	tmp = input("Skriv inn koordinatene til vektoren. Separer koordinater med mellomrom. x y z = ")
	coors = tmp.split()
	for i in range(len(coors)):
		coors[i] = float(coors[i])
	return coors

def getSkalar():
	return int(input("Skriv inn skalar (heltall): "))

def skalarMult (v,s):
	for i in range(len(v)):
		v[i] = v[i]*s
	return v

def getLengde(v):
	sum = 0
	for i in range(len(v)):
		sum += math.pow(v[i],2)
	return math.sqrt(sum)

def finnForskjell (l1, l2):
	if (l1 == l2):
		print("De to vektorene er like lange")
	elif (l1 > l2):
		print("Den første vektoren er ",(l1-l2)," lengre enn den andre",sep='')
	else:
		print("Den andre vektoren er ",(l2-l1)," lengre enn den første",sep='')


def indreProdukt (v1, v2):
	sum = 0
	for i in range(len(v1)):
		sum += v1[i] * v2[i]
	return sum

main()