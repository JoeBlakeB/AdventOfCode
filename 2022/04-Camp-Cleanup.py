#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 4: Camp Cleanup

with open("inputs/04.txt") as f:
    pairs = f.read().strip().split("\n")

fullyContains = 0
anyOverlap = 0

def toSet(elf):
    split = elf.split("-")
    return set(range(int(split[0]), int(split[1]) + 1))

for pair in pairs:
    elves = pair.split(",")
    elves = [toSet(elf) for elf in elves]
    if elves[0].issubset(elves[1]) or elves[1].issubset(elves[0]):
        fullyContains += 1
    if elves[0].intersection(elves[1]):
        anyOverlap += 1
    
print("Fully contains:", fullyContains)
print("Any Overlap:", anyOverlap)
