"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5
"""
import copy
from pathlib import Path

data = (Path(__file__).parents[1] / "input" / "05.txt").read_text()


def part1(stacks: list[list[str]], moves: list[str]) -> str:
    for move in moves:
        m = [int(i) for i in move.split() if i.isdigit()]
        amount = m[0]
        s1 = stacks[m[1] - 1]
        s2 = stacks[m[2] - 1]

        s2.extend(reversed(s1[-amount:]))
        del s1[-amount:]

    top = [i[-1] for i in stacks if i]
    return "".join(top)


def part2(stacks: list[list[str]], moves: list[str]) -> str:
    for move in moves:
        m = [int(i) for i in move.split() if i.isdigit()]
        amount = m[0]
        s1 = stacks[m[1] - 1]
        s2 = stacks[m[2] - 1]

        s2.extend(s1[-amount:])
        del s1[-amount:]

    top = [i[-1] for i in stacks if i]
    return "".join(top)


def main():
    d = data.split("\n\n")
    crates = d[0].splitlines()
    moves = d[1].splitlines()

    num_stacks = int(crates[-1].strip().split(" ")[-1])
    stacks1: list[list[str]] = [[] for _ in range(num_stacks)]

    for l in reversed(crates[:-1]):
        for i, stack in enumerate(stacks1):
            pos = i * 4 + 1
            if l[pos].isalpha():
                stack.append(l[pos])
    stacks2 = copy.deepcopy(stacks1)

    print(f"Part One: {part1(stacks1, moves)}")
    print(f"Part Two: {part2(stacks2, moves)}")


if __name__ == "__main__":
    main()
