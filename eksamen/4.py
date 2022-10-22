s = input()
# IKKE endre koden over her
# Skriv koden din mellom her...

def list_str(s):
    liste = []
    for i in range(3, len(s)-3):
        if s[i-3] == "d" and s[i+3] == "c":
            liste.append(s[i])
    return liste


# ...og her
# IKKE endre koden under her
print(list_str(s))