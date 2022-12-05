#!/usr/bin/env python3

# Day 5: Supply Stacks

with open("inputs/05.txt") as f:
    data = f.read().split("\n\n")
    crateData = data[0].split("\n")[:-1]
    actionData = data[1].split("\n")[:-1]

numberOfStacks = int((len(crateData[0]) + 1) / 4)

crates1 = [[] for i in range(numberOfStacks)]

for row in crateData:
    for i in range(0, len(crates1)):
        if row[i*4+1] != " ":
            crates1[i] = [row[i*4+1]] + crates1[i]

crates2 = [crates1[i].copy() for i in range(numberOfStacks)]

for action in actionData:
    action = action.split(" ")
    countToMove = int(action[1])
    fromStack = int(action[3]) - 1
    toStack = int(action[5]) - 1

    # CrateMover9000
    for i in range(countToMove):
        if crates1[fromStack]:
            crates1[toStack].append(crates1[fromStack].pop())

    # CrateMover9001
    cratesPickedUp = []
    for i in range(countToMove):
        if crates2[fromStack]:
            cratesPickedUp = [crates2[fromStack].pop()] + cratesPickedUp
    crates2[toStack] += cratesPickedUp

topCrates = lambda crates: "".join([crates[i][-1] if crates[i] else " " for i in range(numberOfStacks)])

print("CrateMover 9000:", topCrates(crates1))
print("CrateMover 9001:", topCrates(crates2))