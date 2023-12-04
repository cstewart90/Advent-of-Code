"""
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8
"""
import aocd
import numpy as np

data = aocd.get_data(day=8, year=2022)

trees = np.array([list(x) for x in data.splitlines()], int)
visible = np.zeros_like(trees)
scores = np.ones_like(trees)
width, height = trees.shape[0], trees.shape[1]

for _ in range(4):
    for (i, j), tree in np.ndenumerate(trees):
        if i in (0, width - 1) or j in (0, height - 1):
            visible[i, j] = 1
            scores[i, j] = 0
            continue
        elif visible[i, j] == 0 and tree > max(x for x in trees[i, :j]):
            visible[i, j] = 1

        distance = 0
        for distance, t in enumerate(trees[i, j + 1:], start=1):
            if t >= tree:
                break
        scores[i, j] *= distance

    trees = np.rot90(trees)
    visible = np.rot90(visible)
    scores = np.rot90(scores)

print(f"Part One: {np.count_nonzero(visible)}")
print(f"Part Two: {np.max(scores)}")
