"""
--- Day 9: Rope Bridge ---
https://adventofcode.com/2022/day/9
"""

example = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

START = (0, 0)
head = tail = START
visited = {START}

for line in example.splitlines():
    direction, steps = line.split()[0], int(line.split()[1])
    hx, hy = head
    tx, ty = tail

    match direction:
        case "R":
            hx += steps
        case "L":
            hx -= steps
        case "U":
            hy += steps
        case "D":
            hy -= steps

    x = hx - tail[0]
    y = hy - tail[1]

    # if abs(x) > 1 or abs(y) > 1:
    #     if x:
    #
    #     if y:




print(head)
