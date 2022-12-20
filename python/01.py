"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""
from pathlib import Path

data = (Path(__file__).parents[1] / "input" / "01.txt").read_text()

elf_cals: list[int] = []
for d in data.split("\n\n"):
    elf_cals.append(sum(map(int, d.split())))

print(max(elf_cals))
print(sum(sorted(elf_cals, reverse=True)[:3]))
