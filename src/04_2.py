from utils.api import get_input

## Solution du jour 04 - Partie 2
# Retirer itérativement les rouleaux accessibles jusqu'à ce qu'aucun ne soit plus accessible
# Un rouleau est accessible si moins de 4 rouleaux sont dans ses 8 positions adjacentes
# 1. Parser la grille et la copier pour modification
# 2. Répéter : trouver les rouleaux accessibles, les retirer, compter
# 3. Arrêter quand aucun rouleau n'est plus accessible

input_str = get_input(4)
lines = input_str.split("\n")
grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

total_removed = 0

while True:
    # Trouver tous les rouleaux accessibles
    accessible = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                adjacent_rolls = sum(
                    1
                    for dr, dc in directions
                    if 0 <= r + dr < rows
                    and 0 <= c + dc < cols
                    and grid[r + dr][c + dc] == "@"
                )
                if adjacent_rolls < 4:
                    accessible.append((r, c))

    # Si aucun rouleau accessible, arrêter
    if not accessible:
        break

    # Retirer tous les rouleaux accessibles
    for r, c in accessible:
        grid[r][c] = "."

    total_removed += len(accessible)

print(total_removed)
