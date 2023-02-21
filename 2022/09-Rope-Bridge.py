#!/usr/bin/env python3

# Day 9: Rope Bridge

with open("inputs/09.txt") as f:
    data = [line.split(" ") for line in f.read().strip().split("\n")]


calcHeadNewLocation = {
    "R": lambda x, y: [x + 1, y],
    "L": lambda x, y: [x - 1, y],
    "U": lambda x, y: [x, y + 1],
    "D": lambda x, y: [x, y - 1]
}

def simulateRope(knots=2):
    rope = []
    for knot in range(knots):
        rope.append([0, 0])
    ropePastPositions = {"0-0": "#"}
    for direction, distance in data:
        for i in range(int(distance)):
            rope[0] = calcHeadNewLocation[direction](rope[0][0], rope[0][1])
            for knot in range(knots-1):
                stillTouching = False
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if rope[knot+1][0] + x == rope[knot][0] and rope[knot+1][1] + y == rope[knot][1]:
                            stillTouching = True
                if not stillTouching:
                    for coord in range(2):
                        if rope[knot][coord] != rope[knot+1][coord]:
                            rope[knot+1][coord] += ((rope[knot][coord] > rope[knot+1][coord]) * 2) - 1
            if not stillTouching:
                ropePastPositions[f"{rope[knot+1][0]}-{rope[knot+1][1]}"] = "#"
    return ropePastPositions


print("Part 1:", len(simulateRope()))
print("Part 2:", len(simulateRope(10)))
