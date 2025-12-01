import os
from api import get_instructions

l = filter(lambda x: "__" not in x and "_1.py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) if len(l) > 0 else 1

instructions_path = f"instructions/{n:02d}.instructions"

if os.path.exists(instructions_path):
    os.remove(instructions_path)
    print(f"Removed cached instructions for day {n}")

get_instructions(n)

# Créer le fichier XX_2.py s'il n'existe pas
part2_path = f"src/{n:02d}_2.py"
if not os.path.exists(part2_path):
    DEFAULT_FILE = f"from utils.api import get_input\n\ninput_str = get_input({n})\n\n# WRITE YOUR SOLUTION HERE\n\n"
    with open(part2_path, "w") as f:
        f.write(DEFAULT_FILE)
    print(f"Created {part2_path} for part 2 solution")
else:
    print(f"{part2_path} already exists")

print(
    f"Instructions for day {n} refreshed successfully (part 2 should now be visible)!"
)
