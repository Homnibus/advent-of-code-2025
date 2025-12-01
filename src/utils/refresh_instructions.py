import os
from api import get_instructions

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) if len(l) > 0 else 1

instructions_path = f"instructions/{n:02d}"

if os.path.exists(instructions_path):
    os.remove(instructions_path)
    print(f"Removed cached instructions for day {n}")

get_instructions(n)
print(
    f"Instructions for day {n} refreshed successfully (part 2 should now be visible)!"
)
