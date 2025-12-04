def test_day04_part1():
    """Test avec l'exemple fourni dans les instructions"""
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

    assert accessible_count == 13, f"Expected 13, got {accessible_count}"


if __name__ == "__main__":
    test_day04_part1()
    print("✓ Test passed!")
