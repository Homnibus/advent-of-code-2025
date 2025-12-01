from utils.api import get_input

input_str = get_input(1)

position = 50
count_zeros = 0

for line in input_str.split("\n"):
    if not line:
        continue

    direction = line[0]
    distance = int(line[1:])

    # Nombre de tours complets (chaque tour passe par 0)
    full_rotations = distance // 100
    count_zeros += full_rotations

    # Distance restante après les tours complets
    remaining = distance % 100

    if direction == "L":
        # On passe par 0 si on descend jusqu'à 0 ou en dessous
        # MAIS PAS si on est déjà sur 0 (on part de 0, on ne passe pas par)
        if position > 0 and remaining >= position:
            count_zeros += 1
        position = (position - distance) % 100
    else:  # 'R'
        # On passe par 0 si on dépasse 99
        # MAIS PAS si on est sur 0 (on part de 0, on ne passe pas par)
        if position > 0 and position + remaining >= 100:
            count_zeros += 1
        position = (position + distance) % 100

print(count_zeros)
