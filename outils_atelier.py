def compter(liste):
    combien = 0
    for nombre in liste:
        combien = combien + 1
    return combien


def plus_long(liste):
    if len(liste) == 0:
        return None
    long = liste[0]
    for mot in liste:
        if len(mot) > len(long):
            long = mot
    return long


def noms_courts(liste,limite):
    court = []
    for nom in liste:
        if len(nom) < limite:
            court.append(nom)
    return court


def total_caracteres(liste):
    compte = 0
    for mot in liste:
        for caractere in mot:
            compte = compte + 1
    return compte




