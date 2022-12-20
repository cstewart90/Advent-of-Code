"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
"""
from pathlib import Path

data = (Path(__file__).parents[1] / "input" / "02.txt").read_text()

# X is Rock, Y is Paper, Z is Scissors
points = {"X": 1, "Y": 2, "Z": 3}

# A is Rock, B is Paper, C is Scissors
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}

part1 = 0
part2 = 0
for x in data.splitlines():
    opp, me = x.split()

    # part 1
    if win[opp] == me:
        part1 += 6
    elif draw[opp] == me:
        part1 += 3

    part1 += points[me]

    # part 2
    if me == "X":
        # need to lose
        move = lose[opp]
        part2 += points[move]
    elif me == "Y":
        # need to draw
        move = draw[opp]
        part2 += points[move] + 3
    else:
        # need to win
        move = win[opp]
        part2 += points[move] + 6

print(f"Part One: {part1}")
print(f"Part Two: {part2}")
