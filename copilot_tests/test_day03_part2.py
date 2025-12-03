# Test avec l'exemple de l'énoncé - Partie 2
# Pour chaque banque de batteries, trouver le voltage maximum en allumant 12 batteries
# Résultat attendu: 3121910778619

test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""


def find_max_joltage_k_batteries(bank, k):
    """
    Trouve le voltage maximum en sélectionnant exactement k batteries.
    Utilise un algorithme de pile pour trouver la plus grande sous-séquence de longueur k.
    """
    n = len(bank)
    to_remove = n - k  # Nombre de chiffres à retirer

    stack = []

    for i, digit in enumerate(bank):
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

print("=== Analyse détaillée - Partie 2 ===")
for line in test_input.split("\n"):
    if not line:
        continue

    max_joltage = find_max_joltage_k_batteries(line, 12)
    total += max_joltage

    print(f"{line} ({len(line)} chiffres): voltage max = {max_joltage}")

print(f"\n=== Résultat final: {total} ===")
print("Attendu: 3121910778619")
