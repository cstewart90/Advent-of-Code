"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""
from collections import defaultdict
from pathlib import Path, PurePosixPath


def populate_dirs(data):
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
    data = (Path(__file__).parents[1] / "input" / "07.txt").read_text()
    dirs = populate_dirs(data)

    part1 = sum(d for d in dirs.values() if d <= 100_000)
    print(f"Part One: {part1}")

    target = dirs[PurePosixPath("/")] + 30_000_000 - 70_000_000
    part2 = min(d for d in dirs.values() if d >= target)
    print(f"Part Two: {part2}")


if __name__ == "__main__":
    main()
