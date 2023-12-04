"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""
import aocd

data = aocd.get_data(day=6, year=2022)


def find_marker(signal: str, marker_len: int):
    for i in range(marker_len - 1, len(signal)):
        seq = set(signal[i - marker_len:i])
        if len(seq) == marker_len:
            return i


def main():
    print(f"Part One: {find_marker(data, 4)}")
    print(f"Part Two: {find_marker(data, 14)}")


if __name__ == "__main__":
    main()
