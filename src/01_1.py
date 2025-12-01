from utils.api import get_input

input_str = get_input(1)

## Solution du jour 01 - Partie 1
# Problème : Compter combien de fois le cadran se retrouve sur 0 après une rotation
# Stratégie : Simuler chaque rotation et vérifier si la position finale est 0
# Détails :
#   1. Partir de la position 50
#   2. Pour chaque rotation (L ou R), calculer la nouvelle position modulo 100
#   3. Compter combien de fois la position finale est exactement 0

position = 50
count_zeros = 0

for line in input_str.split("\n"):
    if not line:
        continue

    direction = line[0]
    distance = int(line[1:])

    if direction == "L":
        position = (position - distance) % 100
    else:  # 'R'
        position = (position + distance) % 100

    if position == 0:
        count_zeros += 1

print(count_zeros)
