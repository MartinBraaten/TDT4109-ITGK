matvarer = [['laks', 59, 'middag'], ['kjøttdeig', 25, 'middag'],
            ['ris', 15, 'middag'], ['ost', 99, 'frokost'], ['bønner', 7, 'middag'],
            ['soyasaus', 33, 'middag'],['banan', 4, 'mellommåltid']]
vare = input()
# IKKE endre koden over her
# Skriv koden din mellom her...

def finn_pris(matvarer, let_etter):
    for i in matvarer:
        if i[0] == let_etter:
            return i[1]



# ...og her
# IKKE endre koden under her
print(finn_pris(matvarer, vare))