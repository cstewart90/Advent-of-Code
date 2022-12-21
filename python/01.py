"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""
import aocd

data = aocd.get_data(day=1, year=2022)

elf_cals: list[int] = []
for d in data.split("\n\n"):
    elf_cals.append(sum(map(int, d.split())))

print(max(elf_cals))
print(sum(sorted(elf_cals, reverse=True)[:3]))
