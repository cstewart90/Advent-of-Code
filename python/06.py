"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""
import aocd

data = aocd.get_data(day=6, year=2022)


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
    print(f"Part One: {part1(data)}")
    print(f"Part Two: {part2(data)}")


if __name__ == "__main__":
    main()
