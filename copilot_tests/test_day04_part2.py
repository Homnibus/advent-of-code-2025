def test_day04_part2():
    """Test avec l'exemple fourni dans les instructions de la partie 2"""
    input_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    lines = input_data.split("\n")
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total_removed = 0

    while True:
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

        if not accessible:
            break

        for r, c in accessible:
            grid[r][c] = "."

        total_removed += len(accessible)

    assert total_removed == 43, f"Expected 43, got {total_removed}"


if __name__ == "__main__":
    test_day04_part2()
    print("✓ Test passed!")
