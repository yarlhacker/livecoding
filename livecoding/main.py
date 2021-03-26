import random


def demander_nombre(nb_min, nb_max):
    # quel est le nombre magique (entre 1 et 10)
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = int(input('entrez votre mise'))


nombre = 200
vies = NB_VIES
if vies > 50:
    while nombre >= NB_VIES :
        print(f"vous miser {NB_VIES} ")
        nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
        if nombre == NOMBRE_MAGIQUE:
            print("Bravo, vous avez gagné")
        else:
            print("Le nombre magique est plus grand")
    if vies == 0:
        print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")
else:
    print("votre mise est moins de 50")
# gagne = False
# for i in range(0, NB_VIES):
#     vies = NB_VIES-i
#     print(f"Il vous reste {vies} vies")
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     if nombre == NOMBRE_MAGIQUE:
#         print("Bravo, vous avez gagné")
#         gagne = True
#         break
#     elif nombre > NOMBRE_MAGIQUE:
#         print("Le nombre magique est plus petit")
#     else:
#         print("Le nombre magique est plus grand")

# if not gagne:
#     print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")
