# Test avec l'exemple de l'énoncé - Partie 1
# Trouver tous les IDs invalides (séquence répétée 2 fois) et les sommer
# Résultat attendu: 1227775554

test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def generate_invalid_ids_in_range(start, end):
    """Génère tous les IDs invalides dans [start, end]"""
    invalid_ids = []

    for length in range(2, 22, 2):
        half_length = length // 2
        pattern_min = 10 ** (half_length - 1) if half_length > 1 else 1
        pattern_max = 10**half_length - 1

        for pattern in range(pattern_min, pattern_max + 1):
            invalid_id = int(str(pattern) * 2)

            if invalid_id > end:
                break
            if invalid_id >= start:
                invalid_ids.append(invalid_id)

    return invalid_ids


ranges = test_input.split(",")
total = 0

print("=== Analyse détaillée - Partie 1 ===")
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
print("Attendu: 1227775554")
