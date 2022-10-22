streng = input()
# IKKE endre koden over her
# Skriv koden din mellom her...

def sjekk_to(streng):
    if int(streng[0:2])<26 and int(streng[2:4])<13 and int(streng[4:6])<58:
        return 1
    elif int(streng[0:2]) > 25 and int(streng[2:4]) > 12 and int(streng[4:6]) > 58:
        return 30
    elif int(streng[0:2])>25 and int(streng[2:4])>12:
        return 6
    elif int(streng[0:2])>25 and int(streng[4:6])>58:
        return 10
    elif int(streng[0:2])>25:
        return 2
    elif int(streng[2:4])>12:
        return 3
    elif int(streng[4:6])>58:
        return 5






# ...og her
# IKKE endre koden under her
print(sjekk_to(streng))