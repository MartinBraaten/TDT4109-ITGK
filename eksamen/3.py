tl = input()[1:-1].split(',')
liste = [int(n) for n in tl]
# IKKE endre koden over
# Skriv koden din mellom her...


def fjern_dup(liste):
    ikke_dup = [liste[0]]
    for i in range(len(liste)-1):
        if liste[i] != liste[i+1]:
            ikke_dup.append(liste[i+1])
    liste[:] = ikke_dup

# ...og her
# IKKE endre koden under
fjern_dup(liste)
print(liste)