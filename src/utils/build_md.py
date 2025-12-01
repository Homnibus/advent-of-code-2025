import os

base_link = "https://github.com/Homnibus/advent-of-code-2025/blob/main/src/"

solutions = filter(
    lambda x: ".py" in x and "init" not in x and "_" in x, os.listdir("src")
)
solutions = list(solutions)

days = {}
for sol in solutions:
    day_num = sol.split("_")[0]
    if day_num not in days:
        days[day_num] = []
    days[day_num].append(sol)

readme_content = "# Advent of code 2025\n\n## Solutions\n\n"
for day_num in sorted(days.keys()):
    links = []
    for file in sorted(days[day_num]):
        part = file.split("_")[1].replace(".py", "")
        links.append(f"[Part {part}]({base_link}{file})")
    readme_content += f"**Day {int(day_num)}**: {' | '.join(links)}\n"

with open("README.md", "w") as f:
    f.write(
        readme_content
        + "\n---\nInspired from: [advent-of-code-setup](https://github.com/tomfran/advent-of-code-setup)"
    )
