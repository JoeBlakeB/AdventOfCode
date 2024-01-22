#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 23: Unstable Diffusion

class Elf:
    x, y = 0, 0
    otherElves = []

    def __init__(self, pos, otherElves):
        self.x, self.y = pos
        self.otherElves = otherElves

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if isinstance(other, Elf):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        return False

    def checkDirection(self, direction, elfGrid):
        gridX = self.x + direction[0] - elfGrid[1]
        gridY = self.y + direction[1] - elfGrid[2]
        if 0 <= gridX < len(elfGrid[0]) and 0 <= gridY < len(elfGrid[0][0]):
            if elfGrid[0][gridX][gridY] == 1:
                return True
        return False

    def proposeMove(self, directions, elfGrid):
        for direction in ((-1, -1), (-1, 0), (-1, 1), 
                          (0, -1),           (0, 1), 
                          (1, -1), (1, 0), (1, 1)):
            if self.checkDirection(direction, elfGrid):
                break
        else:
            self.moveProposal = None
            return None
        for direction in directions:
            for offset in direction:
                if self.checkDirection(offset, elfGrid):
                    break
            else:
                self.moveProposal = (self.x + direction[0][0], 
                    self.y + direction[0][1])
                return self.moveProposal
        self.moveProposal = None

    def move(self, moveProposals):
        if self.moveProposal == None:
            return
        moveProposals.remove(self.moveProposal)
        if self.moveProposal not in moveProposals:
            self.x, self.y = self.moveProposal
        self.moveProposal = None

class Crater:
    elves = []

    directions = [
        ((-1, 0), (-1, -1), (-1, 1)),
        ((1, 0),  (1, -1),  (1, 1)),
        ((0, -1), (-1, -1), (1, -1)),
        ((0, 1),  (-1, 1),  (1, 1))
    ]

    def __init__(self, file):
        with open(file) as f:
            data = f.read().strip().split("\n")
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] == "#":
                    self.elves.append(Elf((row, col), self.elves))

    def __str__(self):
        return "\n".join(["".join(
            ["#" if cell else "." for cell in row]
        ) for row in self.getGrid()[0]])

    def getGrid(self):
        minX = min(self.elves, key=lambda e: e.x).x
        maxX = max(self.elves, key=lambda e: e.x).x
        minY = min(self.elves, key=lambda e: e.y).y
        maxY = max(self.elves, key=lambda e: e.y).y
        grid = [[0] * (maxY - minY + 1) for _ in range(maxX - minX + 1)]
        for elf in self.elves:
            grid[elf.x - minX][elf.y - minY] = 1
        return grid, minX, minY

    def round(self):
        print("Processing Round", i+1, end="\r")
        moveProposals = []
        elfGrid = self.getGrid()
        for elf in self.elves:
            moveProposals.append(elf.proposeMove(self.directions, elfGrid))
        self.directions = self.directions[1:] + [self.directions[0]]
        for elf in self.elves:
            elf.move(moveProposals[:])


crater = Crater("inputs/23.txt")

for i in range(10):
    crater.round()

print("Number of empty ground tiles:", str(crater).count("."))

lastCrater = ""
while lastCrater != str(crater):
    i += 1
    lastCrater = str(crater)
    crater.round()

print("Number of rounds until diffused:", i+1)
