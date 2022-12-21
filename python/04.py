"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
"""
import aocd

data = aocd.get_data(day=4, year=2022)

part1 = 0
part2 = 0
for d in data.splitlines():
    a, b = d.split(',')

    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    r1 = range(a1, a2 + 1)
    r2 = range(b1, b2 + 1)

    if r1.start in r2 and r1[-1] in r2:
        part1 += 1
    elif r2.start in r1 and r2[-1] in r1:
        part1 += 1

    if r1.start in r2 or r2.start in r1:
        part2 += 1

print(f"Part One: {part1}")
print(f"Part Two: {part2}")
