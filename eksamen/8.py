


def oppdater_beholdning(beholdning, endringer):
    for endring in endringer:
        beholdning[endring[0]] += endring[1]
    return beholdning


