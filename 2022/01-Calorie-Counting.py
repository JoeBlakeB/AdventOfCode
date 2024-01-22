#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 1: Calorie Counting

with open("inputs/01.txt") as f:
    data = f.read()

# Part 1
elfs = [0]
most = 0
for row in data.split("\n"):
    if row == "":
        if elfs[-1] > most:
            most = elfs[-1]
        elfs.append(0)
    else:
        elfs[-1] += int(row)

# Part 2
elfs.sort()
topThree = elfs[-1] + elfs[-2] + elfs[-3]

print("Most calories:", most)
print("Top three:    ", topThree)
