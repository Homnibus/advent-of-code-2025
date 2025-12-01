from utils.api import get_input

input_str = get_input(1)

## Solution du jour 01 - Partie 2
# Problème : Compter combien de fois le cadran passe par 0 pendant ET après chaque rotation
# Stratégie : Pour chaque rotation, calculer les tours complets + vérifier si le déplacement restant traverse 0
# Détails :
#   1. Chaque tour complet (distance >= 100) = 1 passage par 0
#   2. Pour le reste de la distance :
#      - En allant à gauche (L) : on passe par 0 si position actuelle > 0 ET on descend jusqu'à/sous 0
#      - En allant à droite (R) : on passe par 0 si position actuelle > 0 ET on dépasse 99
#   3. Note importante : si on est déjà sur 0, on ne compte pas un passage (on part de 0, on ne passe pas par)

position = 50
count_zeros = 0

for line in input_str.split("\n"):
    if not line:
        continue

    direction = line[0]
    distance = int(line[1:])

    # Chaque tour complet passe par 0
    full_rotations = distance // 100
    count_zeros += full_rotations

    remaining = distance % 100

    if direction == "L":
        # Passage par 0 seulement si on descend depuis une position > 0
        if position > 0 and remaining >= position:
            count_zeros += 1
        position = (position - distance) % 100
    else:  # 'R'
        # Passage par 0 seulement si on dépasse 99 depuis une position > 0
        if position > 0 and position + remaining >= 100:
            count_zeros += 1
        position = (position + distance) % 100

print(count_zeros)
