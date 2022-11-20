from random import randint

def tirage(fois, ensemble):
    """ Séléctionne aléatoirement 'fois' (int) valeur de 'univers' (list).
        Renvoie les valeur en list + les valeurs restantes (en list)"""
    boules_tirees = []
    for i in range(fois):
        event = ensemble[randint(ensemble[0], len(ensemble)-1)]
        boules_tirees.append(event)
        ensemble.remove(event)
    return boules_tirees, ensemble


total_boules = [i for i in range(1, 50)]
print("Liste des boules avant tirage :", total_boules)
results = tirage(5, total_boules)
print("Liste des boules tirées :", results[0])
print("Liste des boules restantes après tirage :", results[1])