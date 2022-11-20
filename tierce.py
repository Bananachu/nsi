from random import randint

def tirage(fois, total):
    """ Séléctionne aléatoirement 'fois' (int) valeur de 'total' (list).
        Renvoie ces valeurs en list."""
    num_tires = []
    for i in range(fois):
        boule = total[randint(0, len(total)-1)]
        num_tires.append(boule)
        total.remove(boule)
    return num_tires


def pronostique(fois, ensemble):
    """ Permet à l'utilisateur de séléctionner 'fois' (int)
        nombre(s) de 'ensemble' (list). Renvoie list de ces valeurs.
        (input sécurisé)"""
    pari = []
    print("entrer le numéro des chevaux sur lesquels vous pariez :")
    for i in range(fois):
        cheval = input("cheval n° : ")
        while (type(cheval) != int):
            print(type(cheval))
            cheval = input("veuillez entrer le numéro du cheval : ")
        cheval = int(cheval)
        while (ensemble.count(cheval) != 1):
            cheval = int(input("Veuillez entrer un cheval participant à la course : "))
        while (pari.count(cheval) == 1):
            cheval = int(input("Vous ne pouvez parier que sur trois chevaux différents : "))
        pari.append(cheval)
    return pari


def juge(result, pari):
    if result == pari:
        return "félicitations, vous avez gagné"
    score = 0
    for e in pari:
        score += result.count(e)
    if score == 3:
        return "bravo, vous avez le tiercé mais dans le désordre"
    return "vous avez perdu"

cent = [i for i in range(1, 100)]
chevaux = tirage(10, cent)
print(chevaux)

pari = pronostique(3, chevaux)
print(pari)

tierce = tirage(3, chevaux)
print("le tiercé : ", tierce)


print(juge(tierce, pari))