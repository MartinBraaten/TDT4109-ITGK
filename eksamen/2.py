tall = float(input())
# IKKE endre koden over
# Skriv koden din mellom her...

def sjekk(tall):
    if tall == int(tall):
        if tall % 2 == 0:
            return "par"
        else:
            return "odde"
    else:
        return "des"

# ...og her
# IKKE endre koden under
print(sjekk(tall))