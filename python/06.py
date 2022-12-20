"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""
from pathlib import Path


def part1(signal: str):
    marker_len = 4
    for i in range(marker_len - 1, len(signal)):
        seq = set(signal[i - marker_len:i])
        if len(seq) == marker_len:
            return i


def part2(signal: str):
    marker_len = 14
    for i in range(marker_len - 1, len(signal)):
        seq = set(signal[i - marker_len:i])
        if len(seq) == marker_len:
            return i


def main():
    data = (Path(__file__).parents[1] / "input" / "06.txt").read_text()
    print(f"Part One: {part1(data)}")
    print(f"Part Two: {part2(data)}")


if __name__ == "__main__":
    main()
