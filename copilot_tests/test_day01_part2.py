# Test avec l'exemple de l'énoncé - Partie 2
# Compte tous les passages par 0 (pendant et après rotations, résultat attendu: 6)
test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

position = 50
count_zeros = 0

print("=== Simulation détaillée - Partie 2 ===")
for line in test_input.split("\n"):
    if not line:
        continue

    direction = line[0]
    distance = int(line[1:])

    old_position = position

    # Nombre de tours complets (chaque tour passe par 0)
    full_rotations = distance // 100
    count_zeros += full_rotations

    # Distance restante après les tours complets
    remaining = distance % 100

    passes_through_zero = False
    if direction == "L":
        # On passe par 0 si on descend jusqu'à 0 ou en dessous
        # MAIS PAS si on est déjà sur 0 (on part de 0, on ne passe pas par)
        if position > 0 and remaining >= position:
            count_zeros += 1
            passes_through_zero = True
        position = (position - distance) % 100
    else:  # 'R'
        # On passe par 0 si on dépasse 99
        # MAIS PAS si on est sur 0 (on part de 0, on ne passe pas par)
        if position > 0 and position + remaining >= 100:
            count_zeros += 1
            passes_through_zero = True
        position = (position + distance) % 100

    print(
        f"{direction}{distance}: {old_position} -> {position} | Full rotations: {full_rotations}, Partial pass: {passes_through_zero}, Total zeros so far: {count_zeros}"
    )

print(f"\n=== Résultat final: {count_zeros} ===")
print("Attendu: 6")
