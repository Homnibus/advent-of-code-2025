# Test avec l'exemple de l'énoncé - Partie 1
# Pour chaque banque de batteries, trouver le voltage maximum en allumant 2 batteries
# Résultat attendu: 357

test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""


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

print("=== Analyse détaillée - Partie 1 ===")
for line in test_input.split("\n"):
    if not line:
        continue

    max_joltage = find_max_joltage(line)
    total += max_joltage

    print(f"{line}: voltage max = {max_joltage}")

print(f"\n=== Résultat final: {total} ===")
print("Attendu: 357")
