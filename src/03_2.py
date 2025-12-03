from utils.api import get_input

input_str = get_input(3)

## Solution du jour 03 - Partie 2
# Problème : Trouver le voltage maximum en allumant exactement 12 batteries par banque
# Stratégie : Utiliser un algorithme de pile greedy pour trouver la plus grande sous-séquence
# Étapes :
# 1. Pour chaque banque, calculer combien de chiffres retirer (n - 12)
# 2. Parcourir les chiffres et utiliser une pile :
#    - Si le sommet de la pile est plus petit que le chiffre actuel et qu'on peut retirer, dépiler
#    - Ajouter le chiffre actuel à la pile
# 3. Si nécessaire, retirer les derniers chiffres pour avoir exactement 12 chiffres
# 4. Convertir la pile en nombre et sommer tous les voltages


def find_max_joltage_k_batteries(bank, k):
    """
    Trouve le voltage maximum en sélectionnant exactement k batteries.
    Utilise un algorithme de pile pour trouver la plus grande sous-séquence de longueur k.
    """
    n = len(bank)
    to_remove = n - k  # Nombre de chiffres à retirer

    stack = []

    for digit in bank:
        # Tant qu'on peut retirer des chiffres et que le sommet de la pile est plus petit
        # que le chiffre actuel, on dépile
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1

        stack.append(digit)

    # Si on doit encore retirer des chiffres, on retire à la fin
    while to_remove > 0:
        stack.pop()
        to_remove -= 1

    # Convertir la pile en nombre
    return int("".join(stack))


total = 0

for line in input_str.split("\n"):
    if line:
        total += find_max_joltage_k_batteries(line, 12)

print(total)
