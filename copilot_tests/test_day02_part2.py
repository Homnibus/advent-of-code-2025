# Test avec l'exemple de l'énoncé - Partie 2
# Trouver tous les IDs invalides (séquence répétée au moins 2 fois) et les sommer
# Résultat attendu: 4174379265

test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


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

    return sorted(list(invalid_ids))


ranges = test_input.split(",")
total = 0

print("=== Analyse détaillée - Partie 2 ===")
for range_str in ranges:
    start, end = map(int, range_str.split("-"))
    invalid_ids = generate_invalid_ids_in_range(start, end)
    range_sum = sum(invalid_ids)
    total += range_sum

    if invalid_ids:
        print(f"{range_str}: {invalid_ids} -> somme = {range_sum}")
    else:
        print(f"{range_str}: aucun ID invalide")

print(f"\n=== Résultat final: {total} ===")
print("Attendu: 4174379265")
