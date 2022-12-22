#!/usr/bin/env python3

# Day 17: Pyroclastic Flow

class Grid:
    towerHeight = 0
    JetSequence = 0
    grid = []
    repeatCount = 0
    optimisedTowerHeight = 0

    def __init__(self):
        with open("inputs/17.txt") as f:
            self.jetData = f.read().strip()

    def __str__(self):
        output = ""
        for row in self.grid[::-1]:
            output += "|" + "".join(".#"[int(i)] for i in row) + "|\n"
        return output + "+-------+"

    def jetDirection(self):
        jet = self.jetData[self.JetSequence]
        self.JetSequence += 1
        if self.JetSequence >= len(self.jetData):
            self.JetSequence = 0
            self.repeatCount += 1
            if self.repeatCount == 2:
                self.towerHeightPerJetSequence = self.towerHeight
            elif self.repeatCount == 3:
                self.towerHeightPerJetSequence = self.towerHeight - self.towerHeightPerJetSequence
        return ((jet == ">")*2)-1

    def isRockColiding(self, rock, rockHeight, rockHorizontal):
        if rockHeight < 0:
            return True
        for y in range(len(rock)):
            for x in range(len(rock[y])):
                try:
                    if rock[y][x] and self.grid[rockHeight + y][rockHorizontal + x]:
                        return True
                except IndexError: pass
        return False

    def addRock(self, rock, rockHeight, rockHorizontal):
        if len(self.grid) < rockHeight + len(rock):
            self.grid += [[0] * 7 for i in range(
                rockHeight + len(rock) - len(self.grid))]
            self.towerHeight = rockHeight + (self.optimisedTowerHeight + len(rock))
        for y in range(len(rock)):
            for x in range(len(rock[y])):
                self.grid[rockHeight + y][rockHorizontal + x] |= rock[y][x]

    def dropRock(self, rock):
        rockHeight = len(self.grid) + 4
        rockHorizontal = 2
        while rockHeight:
            previousRockHorizontal = rockHorizontal
            rockHorizontal += self.jetDirection()
            if (rockHorizontal < 0 or
                rockHorizontal > 7 - len(rock[0]) or
                self.isRockColiding(rock, rockHeight-1, rockHorizontal)):
                rockHorizontal = previousRockHorizontal
            rockHeight -= 1
            if self.isRockColiding(rock, rockHeight-1, rockHorizontal):
                return self.addRock(rock, rockHeight, rockHorizontal)

grid = Grid()

rocks = [
    [[1,1,1,1]],
    [[0,1,0],
     [1,1,1],
     [0,1,0]],
    [[0,0,1],
     [0,0,1],
     [1,1,1]][::-1],
    [[1], [1], [1], [1]],
    [[1,1], [1,1]]
]

for i in range(2022):
    grid.dropRock(rocks[i % len(rocks)])

print("Tower height after 2022 rocks:", grid.towerHeight)

while grid.repeatCount < 2:
    i += 1
    grid.dropRock(rocks[i % len(rocks)])

rocksPerJetSequence = i

while grid.repeatCount < 3:
    i += 1
    grid.dropRock(rocks[i % len(rocks)])

rocksPerJetSequence = i - rocksPerJetSequence
skippedJetSequences = (1000000000000 - grid.towerHeight) // rocksPerJetSequence
i += skippedJetSequences * rocksPerJetSequence
grid.optimisedTowerHeight += skippedJetSequences * grid.towerHeightPerJetSequence

while i < 999999999999:
    i += 1
    grid.dropRock(rocks[i % len(rocks)])

print("Tower height after 1 trillion rocks:", grid.towerHeight)
