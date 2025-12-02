from utils.api import get_input

## Solution du jour 02
# Problème : Identifier et sommer les IDs invalides (nombres formés d'une séquence répétée 2 fois)
# Stratégie : Génération directe des IDs invalides plutôt que brute force
# Pour chaque longueur paire possible (2, 4, 6, ...):
#   - Générer tous les patterns de longueur/2 chiffres
#   - Doubler chaque pattern pour créer un ID invalide (ex: 123 -> 123123)
#   - Vérifier si l'ID est dans la plage [start, end]
#   - Sommer tous les IDs invalides trouvés


def generate_invalid_ids_in_range(start, end):
    """Génère tous les IDs invalides dans [start, end] en testant toutes les longueurs paires"""
    invalid_ids = []

    # Tester toutes les longueurs paires possibles
    for length in range(
        2, 22, 2
    ):  # 22 chiffres suffisent pour couvrir les grands nombres
        half_length = length // 2

        # Plage des patterns pour cette longueur
        pattern_min = 10 ** (half_length - 1) if half_length > 1 else 1
        pattern_max = 10**half_length - 1

        for pattern in range(pattern_min, pattern_max + 1):
            # Créer l'ID invalide
            invalid_id = int(str(pattern) * 2)

            # Vérifier si dans la plage
            if invalid_id > end:
                break  # Plus besoin de tester pour cette longueur
            if invalid_id >= start:
                invalid_ids.append(invalid_id)

    return invalid_ids


input_str = get_input(2)

ranges = input_str.split(",")
total = 0

for range_str in ranges:
    start, end = map(int, range_str.split("-"))
    invalid_ids = generate_invalid_ids_in_range(start, end)
    total += sum(invalid_ids)

print(total)
