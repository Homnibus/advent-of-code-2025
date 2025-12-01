# Test avec l'exemple de l'énoncé - Partie 1
# Compte uniquement les positions finales à 0 (résultat attendu: 3)
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

print("=== Simulation détaillée - Partie 1 ===")
for line in test_input.split("\n"):
    if not line:
        continue

    direction = line[0]
    distance = int(line[1:])

    old_position = position

    if direction == "L":
        position = (position - distance) % 100
    else:  # 'R'
        position = (position + distance) % 100

    if position == 0:
        count_zeros += 1

    print(
        f"{direction}{distance}: {old_position} -> {position} | Zeros count: {count_zeros}"
    )

print(f"\n=== Résultat final: {count_zeros} ===")
print("Attendu: 3")
