from utils.api import get_input

## Solution du jour 04
# Trouver les rouleaux de papier (@) accessibles par un chariot élévateur
# Un rouleau est accessible si moins de 4 rouleaux sont dans ses 8 positions adjacentes
# 1. Parser la grille depuis l'input
# 2. Pour chaque @, compter les @ voisins dans les 8 directions
# 3. Compter les rouleaux avec strictement moins de 4 voisins

input_str = get_input(4)
lines = input_str.split("\n")
grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# 8 directions : diagonales + cardinales
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

accessible_count = 0

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
                accessible_count += 1

print(accessible_count)
