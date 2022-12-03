#!/usr/bin/env python3

# Day 3: Rucksack Reorganization

with open('inputs/03.txt') as f:
    elves = f.read().strip().split("\n")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sumOfPriorities1 = 0
sumOfPriorities2 = 0

# Task 1

for rucksack in elves:
    compartments = [
        rucksack[0:len(rucksack)//2],
        rucksack[len(rucksack)//2:]]
    for item in compartments[0]:
        if item in compartments[1]:
            sumOfPriorities1 += alphabet.index(item) + 1
            break

# Task 2

for i in range(0, len(elves), 3):
    group = elves[i:i+3]
    for item in group[0]:
        if item in group[1] and item in group[2]:
            sumOfPriorities2 += alphabet.index(item) + 1
            break
            
print(sumOfPriorities1) # 7980
print(sumOfPriorities2) # 0