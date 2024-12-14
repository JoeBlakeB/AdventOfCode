#!/usr/bin/env python3
# Copyright (C) 2024 Joe Baker (JoeBlakeB)
# Advent of Code 2024 - Day 14: Restroom Redoubt
# Usage:
#     python 2024/14-Restroom-Redoubt.py < 2024/inputs/14.txt

import re
import sys
from math import prod

WIDTH = 101
HEIGHT = 103

class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = int(px)
        self.py = int(py)
        self.vx = int(vx)
        self.vy = int(vy)

    def simulate(self, seconds):
        self.px += self.vx * seconds
        self.py += self.vy * seconds
        self.px %= WIDTH
        self.py %= HEIGHT

    def __repr__(self):
        return f"p={self.px},{self.py} v={self.vx},{self.vy}"

robots = [Robot(*re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0]) for line in iter(lambda: next(sys.stdin).rstrip("\n"), "")]

quadrants = [0, 0, 0, 0]

for robot in robots:
    robot.simulate(100)
    if robot.px != WIDTH // 2 and robot.py != HEIGHT // 2:
        quadrants[int(robot.px < WIDTH // 2)*2 + int(robot.py < HEIGHT // 2)] += 1

secondsPassed = 100

while True:
    grid = [["." for i in range(WIDTH)] for i in range(HEIGHT)]
    for robot in robots:
        grid[robot.py][robot.px] = "#"
    gridStr = "\n".join((("".join(line)) for line in grid))
    
    if "#########################" in gridStr:
        break

    secondsPassed += 1
    for robot in robots:
        robot.simulate(1)

print(gridStr)
print("Safety Factor:", prod(quadrants))
print("Seconds to find Tree:", secondsPassed)
