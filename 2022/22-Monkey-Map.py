#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
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


class Cube(Board):
    wrapMappings = {
        ((49,), range(0, 50), Board.directions[2]):
            lambda pos: ((0, 99 + (50 - pos[1])), 2),
        ((-1,), range(100, 150), Board.directions[2]):
            lambda pos: ((50, 50 - (pos[1] - 99)), 2),

        (range(50, 100), (-1,), Board.directions[3]):
            lambda pos: ((0, 100 + pos[0]), 1),
        ((-1,), range(150, 200), Board.directions[2]):
            lambda pos: ((pos[1] - 100, 0), -1),

        ((50,), range(150, 200), Board.directions[0]):
            lambda pos: ((pos[1] - 100, 149), -1),
        ((range(50, 100), (150,), Board.directions[1])):
            lambda pos: ((49, 100 + pos[0]), 1),

        ((150,), range(0, 50), Board.directions[0]):
            lambda pos: ((99, 99 + (50 - pos[1])), 2),
        ((100,), range(100, 150), Board.directions[0]):
            lambda pos: ((149, 50 - (pos[1] - 99)), 2),

        (range(100, 150), (-1,), Board.directions[3]):
            lambda pos: ((pos[0] - 100, 199), 0),
        (range(0, 50), (200,), Board.directions[1]):
            lambda pos: ((100 + pos[0], 0), 0),

        ((49,), range(50, 100), Board.directions[2]):
            lambda pos: ((pos[1] - 50, 100), -1),
        (range(0, 50), (99,), Board.directions[3]):
            lambda pos: ((50, 50 + pos[0]), 1),

        (range(100, 150), (50,), Board.directions[1]):
            lambda pos: ((99, pos[0] - 50), 1),
        ((100,), range(50, 100), Board.directions[0]):
            lambda pos: ((100 + (pos[1] - 50), 49), -1)
    }

    def wrap(self, position, direction):
        for key in self.wrapMappings:
            if position[0] in key[0] and position[1] in key[1] and direction == key[2]:
                return self.wrapMappings[key](position)
        raise Exception("No wrap found for position " + str(position) + " and direction " + str(direction) + ", wrap mappings only work on the real input.")


sequence = re.findall(r"(\d+|R|L)", sequence)

print("Board password:", Board(mapData).getPassword(sequence))

print("Cube password:", Cube(mapData).getPassword(sequence))
