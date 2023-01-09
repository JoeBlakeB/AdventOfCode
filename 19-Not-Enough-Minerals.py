#!/usr/bin/env python3

# Day 19: Not Enough Minerals

import re

class Blueprint:
    costs = (0, 0, 0, 0)
    robots = [1, 0, 0, 0]
    materials = [0, 0, 0, 0]
    mostRobotsNeeded = [0, 0, 0, 0]

    def __init__(self, data):
        self.costs = (
            int(data[1]),
            int(data[2]),
            (int(data[3]), int(data[4])),
            (int(data[5]), int(data[6]))
        )

        self.mostRobotsNeeded = [
            max((self.costs[0], self.costs[1], self.costs[2][0], self.costs[3][0])),
            self.costs[2][1],
            self.costs[3][1],
            1000
        ]

    def __repr__(self):
        return f"Blueprint {self.id} {self.costs}"

    canMake = [
        (lambda self, materials: materials[0] >= self.costs[0]),
        (lambda self, materials: materials[0] >= self.costs[1]),
        (lambda self, materials: materials[0] >= self.costs[2][0] and materials[1] >= self.costs[2][1]),
        (lambda self, materials: materials[0] >= self.costs[3][0] and materials[2] >= self.costs[3][1])
    ]

    makeRobot = [
        lambda self, materials: [materials[0] - self.costs[0], materials[1], materials[2], materials[3]],
        lambda self, materials: [materials[0] - self.costs[1], materials[1], materials[2], materials[3]],
        lambda self, materials: [materials[0] - self.costs[2][0], materials[1] - self.costs[2][1], materials[2], materials[3]],
        lambda self, materials: [materials[0] - self.costs[3][0], materials[1], materials[2] - self.costs[3][1], materials[3]]
    ]

    simulateCache = {}

    def simulate(self, robots, materials, minutesRemaining):
        cacheKey = str((robots, materials))
        if cacheKey in self.simulateCache[minutesRemaining]:
            return self.simulateCache[minutesRemaining][cacheKey]

        lastMaterials = materials.copy()
        for i in range(4):
            materials[i] += robots[i]
        if minutesRemaining == 0:
            return materials[3]

        if (self.canMake[0](self, lastMaterials) and self.canMake[1](self, lastMaterials) and
            (self.canMake[2](self, lastMaterials) or robots[1] == 0) and
            (self.canMake[3](self, lastMaterials) or robots[2] == 0)):
            geodes = []
        else:
            geodes = [self.simulate(robots, materials.copy(), minutesRemaining - 1)]

        for i in range(4):
            if self.canMake[i](self, lastMaterials) and robots[i] < self.mostRobotsNeeded[i] and materials[i] < self.mostRobotsNeeded[i] * minutesRemaining:
                newRobots = robots.copy()
                newRobots[i] += 1
                newMaterials = self.makeRobot[i](self, materials)
                geodes.append(self.simulate(newRobots, newMaterials, minutesRemaining - 1))
        
        if geodes:
            self.simulateCache[minutesRemaining][cacheKey] = max(geodes)
            return max(geodes)
        else:
            self.simulateCache[minutesRemaining][cacheKey] = 0
            return 0

    def getMostGeodes(self, minutes=24):
        self.simulateCache = {i: {} for i in range(minutes)}
        mostGeodes = self.simulate(self.robots, self.materials.copy(), minutes-1)
        del self.simulateCache
        return mostGeodes
    

with open("inputs/19.txt") as f:
    data = f.read().strip()

blueprints = [Blueprint(re.findall(r"(\d+)", d)) for d in data.split("\nBlueprint")]

qualitySum = 0
for i in range(len(blueprints)):
    print(f"Calculating: {i+1}/{len(blueprints)}", end="\r")
    qualitySum += blueprints[i].getMostGeodes() * (i+1)

print("Sum of all blueprints quality:", qualitySum)

blueprints = blueprints[:3]
geodeProduct = 1
for i in range(len(blueprints)):
    print(f"Calculating: {i+1}/{len(blueprints)}", end="\r")
    geodeProduct *= blueprints[i].getMostGeodes(32)

print("The product of the blueprints that werent eaten:", geodeProduct)
