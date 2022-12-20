"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3
"""
from pathlib import Path

data = (Path(__file__).parents[1] / "input" / "03.txt").read_text()


def part1(rucksacks: list[str]) -> int:
    total = 0
    for r in rucksacks:
        c1 = r[:len(r) // 2]
        c2 = r[len(r) // 2:]

        item = max(set(c1).intersection(c2))
        total += priority(item)
    return total


def part2(rucksacks: list[str]) -> int:
    total = 0
    for r1, r2, r3 in zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3]):
        badge = max(set(r1).intersection(r2, r3))
        total += priority(badge)
    return total


def priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


print(f"Part One: {part1(data.splitlines())}")
print(f"Part Two: {part2(data.splitlines())}")
