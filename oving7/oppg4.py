__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

    #Sortering

#a) Skriv funksjonen bubbleSort(), forklart under.

 #Bubblesort: Velger første tall: er det større en det neste tallet? Hvis ja: bytt plass. Gå så til neste tall, gjenta.
 # Gjør dette til du har gått gjennom hele listen uten å bytte. Mer informasjon finnes om Boblesortering her.


liste=[1,20,5,17,12,32,17,7,3,2,7]
def bubble(liste):
    for i in range(0,len(liste)):
        swapped = False
        for element in range(0, len(liste)-i-1):
            if liste[element] > liste[element + 1]:
                hold = liste[element + 1]
                liste[element + 1] = liste[element]
                liste[element] = hold
                swapped = True
        if not swapped: break

    print(liste)
bubble(liste)

#b) Skriv funksjonen selectionSort(), forklart under.

#Selectionsort: Finn det største tallet i liste og plasser det på første plass i en ny liste, fjern deretter tallet fra den opprinnelige listen, gjenta.
# Mer informasjon finnes om Selection sort, se også under Insertion_sort.

def selectionSort(liste):
    nyliste=[]



    print(nyliste)
selectionSort(liste)