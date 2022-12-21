"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""
from collections import defaultdict
from pathlib import PurePosixPath

import aocd

data = aocd.get_data(day=7, year=2022)


def populate_dirs():
    dirs = defaultdict(int)
    path = PurePosixPath()
    for line in data.splitlines():
        match line.split():
            case ("$", "cd", ".."):
                path = path.parent
            case ("$", "cd", d):
                path = path.joinpath(d)
            case (size, _) if size.isdigit():
                dirs[path] += int(size)
                for p in path.parents:
                    dirs[p] += int(size)
    return dirs


def main():
    dirs = populate_dirs()

    part1 = sum(d for d in dirs.values() if d <= 100_000)
    print(f"Part One: {part1}")

    target = dirs[PurePosixPath("/")] + 30_000_000 - 70_000_000
    part2 = min(d for d in dirs.values() if d >= target)
    print(f"Part Two: {part2}")


if __name__ == "__main__":
    main()
