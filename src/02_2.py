from utils.api import get_input

## Solution du jour 02 - Partie 2
# Problème : Identifier les IDs invalides (séquence répétée au moins 2 fois)
# Stratégie : Génération par diviseurs de longueur
# Pour chaque longueur L, tester tous ses diviseurs D où L/D >= 2
# Générer les patterns de longueur D répétés L/D fois
# Utiliser un set pour éviter les doublons (ex: 111111 = 1×6 = 11×3 = 111×2)


def generate_invalid_ids_in_range(start, end):
    """Génère tous les IDs invalides (pattern répété ≥2 fois) dans [start, end]"""
    invalid_ids = set()

    for length in range(2, 22):
        # Trouver tous les diviseurs de length
        for pattern_length in range(1, length):
            if length % pattern_length != 0:
                continue

            repetitions = length // pattern_length
            if repetitions < 2:
                continue

            # Générer les patterns
            pattern_min = 10 ** (pattern_length - 1) if pattern_length > 1 else 1
            pattern_max = 10**pattern_length - 1

            for pattern in range(pattern_min, pattern_max + 1):
                invalid_id = int(str(pattern) * repetitions)

                if invalid_id > end:
                    break
                if invalid_id >= start:
                    invalid_ids.add(invalid_id)

    return list(invalid_ids)


input_str = get_input(2)

ranges = input_str.split(",")
total = 0

for range_str in ranges:
    start, end = map(int, range_str.split("-"))
    invalid_ids = generate_invalid_ids_in_range(start, end)
    total += sum(invalid_ids)

print(total)
