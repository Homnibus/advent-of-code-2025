from utils.api import get_input

input_str = get_input(3)

## Solution du jour 03
# Problème : Trouver le voltage maximum de chaque banque de batteries
# Stratégie : Pour chaque banque, tester toutes les paires de batteries possibles
# Étapes :
# 1. Pour chaque ligne (banque), parcourir toutes les paires (i, j) où i < j
# 2. Calculer le voltage formé par les deux chiffres : chiffre[i]*10 + chiffre[j]
# 3. Garder le voltage maximum de chaque banque
# 4. Sommer tous les voltages maximums


def find_max_joltage(bank):
    """Trouve le voltage maximum pour une banque de batteries"""
    max_joltage = 0

    # Tester toutes les paires possibles de positions (i, j) où i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Le voltage est formé par les deux chiffres
            joltage = int(bank[i]) * 10 + int(bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage


total = 0

for line in input_str.split("\n"):
    if line:
        total += find_max_joltage(line)

print(total)
