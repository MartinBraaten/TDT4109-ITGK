beholdning = {'laks': 6, 'kjøttdeig': 14, 'ris': 15, 'ost': 9, 'bønner': 6, 'soyasaus': 0, 'banan': 1}
vare = input()
tall = int(input())
# IKKE endre koden over her
# Skriv koden din mellom her...

def oppdater_matvare(beholdning, matvare, antall):
    beholdning[matvare] += antall
    return beholdning[matvare]



# ...og her
# IKKE endre koden under her
oppdater_matvare(beholdning, vare, tall)
print(beholdning[vare])