import outils_atelier
outils = ["marteau", "scie", "burin", "tournevis", "pince", "niveau"]


def test_compter():
    assert outils_atelier.compter(outils) == 6


def test_plus_long():
    assert outils_atelier.plus_long(outils) == "tournevis"


def test_noms_courts():
    assert outils_atelier.noms_courts(outils,6) == ['scie', 'burin', 'pince']


def test_total_caracteres():
    assert outils_atelier.total_caracteres(outils) == 36


# Dans ce fichier tous les test passent . ca prouve que ma fonction fonctionne mais cela ne prouve pas 
# qu'elle fonctionne sur le but pour laquelle elle a ete créé car elle ne met pas en etude ce point.