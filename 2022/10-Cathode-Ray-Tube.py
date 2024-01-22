#!/usr/bin/env python3
# Copyright (C) 2022 Joe Baker (JoeBlakeB)
# Day 10: Cathode-Ray Tube

with open("inputs/10.txt") as f:
    data = f.read().strip()

xRegister = 1
signalStrengthSum = 0
instructions = data.replace("addx", "wait\naddx").split("\n")
crt = [["░" for i in range(40)] for i in range(6)]

for cycleCounter in range(len(instructions)):
    # Part 1 - Signal Sum
    if not (cycleCounter + 21) % 40:
        signalStrengthSum += xRegister * (cycleCounter+1)

    # Part 2 - Render Image
    if xRegister-1 <= cycleCounter % 40 <= xRegister+1:
        crt[cycleCounter//40][cycleCounter % 40] = "▓"

    if instructions[cycleCounter][:4] == "addx":
        xRegister += int(instructions[cycleCounter][5:])

print("The sum of the signals:", signalStrengthSum)
print("The rendered image on the CRT:")
for row in crt:
    print("".join(row))