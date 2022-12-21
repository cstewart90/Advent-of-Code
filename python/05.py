"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5
"""
import copy
from pathlib import Path

data = (Path(__file__).parents[1] / "input" / "05.txt").read_text()


def move_crates(stacks: list[list[str]], moves: list[str], part2=False) -> str:
    for move in moves:
        amount, src, dest = [int(i) for i in move.split() if i.isdigit()]
        src -= 1
        dest -= 1

        stacks[src], c = stacks[src][:-amount], stacks[src][-amount:]

        if not part2:
            c.reverse()
        stacks[dest].extend(c)

    top = [i[-1] for i in stacks if i]
    return "".join(top)


def main():
    d = data.split("\n\n")
    crates = d[0].splitlines()
    moves = d[1].splitlines()

    num_stacks = int(crates[-1].strip().split(" ")[-1])
    stacks1: list[list[str]] = [[] for _ in range(num_stacks)]

    for crate in reversed(crates[:-1]):
        for i, stack in enumerate(stacks1):
            pos = i * 4 + 1
            if crate[pos].isalpha():
                stack.append(crate[pos])
    stacks2 = copy.deepcopy(stacks1)

    print(f"Part One: {move_crates(stacks1, moves)}")
    print(f"Part Two: {move_crates(stacks2, moves, part2=True)}")


if __name__ == "__main__":
    main()
