#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Day 24: Blizzard Basin

class Valley:
    blizzards = []
    expeditions = set()
    width = 0
    height = 0
    blizzardDirections = {
        "^": [0, -1],
        "v": [0, 1],
        ">": [1, 0],
        "<": [-1, 0]
    }

    def __init__(self, filename):
        with open(filename) as f:
            data = f.read().strip().split("\n")
        self.width = len(data[0]) - 2
        self.height = len(data) - 2
        for y in range(1, self.height + 1):
            blizzardRow = []
            for x in range(1, self.width + 1):
                if data[y][x] != ".":
                    blizzardRow.append([[data[y][x], 
                        self.blizzardDirections[data[y][x]]]])
                else:
                    blizzardRow.append([])
            self.blizzards.append(blizzardRow)
    
    def __str__(self):
        output = []
        for row in self.blizzards:
            rowOut = []
            for blizzard in row:
                if len(blizzard) == 0:
                    rowOut += ["."]
                elif len(blizzard) == 1:
                    rowOut += [blizzard[0][0]]
                else:
                    rowOut += [str(len(blizzard))]
            output.append(rowOut)
        for expedition in self.expeditions:
            if 0 <= expedition[1] < self.height and 0 <= expedition[0] < self.width:
                output[expedition[1]][expedition[0]] = "X"
        return "\n".join(["".join(row) for row in output])

    def moveBlizzards(self):
        newBlizzards = [[[] for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                for blizzard in self.blizzards[y][x]:
                    newY = (y + blizzard[1][1]) % self.height
                    newX = (x + blizzard[1][0]) % self.width
                    newBlizzards[newY][newX].append(blizzard)
        self.blizzards = newBlizzards
    
    def newExpeditions(self):
        newExpeditions = set()
        for expedition in self.expeditions:
            newExpeditions.update([expedition,
                (expedition[0] + 1, expedition[1]),
                (expedition[0] - 1, expedition[1]),
                (expedition[0], expedition[1] + 1),
                (expedition[0], expedition[1] - 1)])
        if self.end in newExpeditions:
            return False
        for expedition in tuple(newExpeditions):
            if (not (0 <= expedition[1] < self.height and 0 <= expedition[0] < self.width) or
                len(self.blizzards[expedition[1]][expedition[0]]) != 0) and expedition != self.start:
                    newExpeditions.remove(expedition)
        return newExpeditions

    def crossValley(self, start, end):
        self.expeditions = {start}
        self.start = start
        self.end = end
        minutes = 0
        while True:
            minutes += 1
            self.moveBlizzards()
            newExpeditions = self.newExpeditions()
            if not newExpeditions:
                return minutes
            self.expeditions = newExpeditions

valley = Valley("inputs/24.txt")

minutes = valley.crossValley((0, -1), (valley.width-1, valley.height))

print("Time to cross the valley:", minutes, "minutes")

minutes += valley.crossValley((valley.width-1, valley.height), (0, -1))
minutes += valley.crossValley((0, -1), (valley.width-1, valley.height))

print("Time to go back for snacks:", minutes, "minutes")
