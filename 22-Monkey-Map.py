#!/usr/bin/env python3

# Day 22: Monkey Map

import re

with open("inputs/22.txt") as f:
    mapData, sequence = f.read().split("\n\n")

class Board:
    map = []
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    height = 0
    width = 0

    def __init__(self, map):
        self.map = map.split("\n")
        self.height = len(self.map)
        self.width = max([len(row) for row in self.map])
    
    def getPassword(self, sequence):
        position = (self.map[0].index("."), 0)
        direction = 0
        for step in sequence:
            if step in ("L", "R"):
                direction = (direction + (1 if step[-1] == "R" else -1)) % 4
            else:
                posDir = self.directions[direction]
                for i in range(int(step)):
                    newPos, newDir = self.move(position, posDir)
                    if self.map[newPos[1]][newPos[0]] == ".":
                        position = newPos
                        direction = (direction + newDir) % 4
                        posDir = self.directions[direction]
                    else:
                        break
        return (1000 * (position[1] + 1)) + (4 * (position[0] + 1)) + direction

    def move(self, position, direction):
        newPos = (position[0] + direction[0], position[1] + direction[1])
        if newPos[0] < 0 or newPos[1] < 0 or newPos[1] >= len(self.map) or newPos[0] >= len(self.map[newPos[1]]) or self.map[newPos[1]][newPos[0]] == " ":
            return self.wrap(newPos, direction)
        return newPos, 0

    def cellValue(self, position):
        row = self.map[position[1] % self.height]
        if position[0] >= len(row) or position[0] < 0 or position[1] < 0:
            return " "
        return row[position[0] % len(row)]

    def wrap(self, position, direction):
        newPos = lambda pos, dir : ((pos[0] + dir[0]) % self.width, (pos[1] + dir[1]) % self.height)
        while self.cellValue(position) == " ":
            position = newPos(position, direction)
        return newPos(position, (0,0)), 0

sequence = re.findall(r"(\d+|R|L)", sequence)

print("Board password:", Board(mapData).getPassword(sequence))
