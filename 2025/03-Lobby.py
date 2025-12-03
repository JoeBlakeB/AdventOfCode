#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 3: Lobby
# Usage:
#     python 2025/03-Lobby.py < 2025/inputs/03.txt

import sys

BATTERY_BANKS = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))


def turnOnTwoBatteries(bank):
    for x in range (9, 0, -1):
        right = str(x).join(bank.split(str(x))[1:])
        if right == bank:
            continue
        for y in range (9, 0, -1):
            if str(y) in right:
                return x*10 + y

print("joules with two batteries per bank:", sum([turnOnTwoBatteries(bank) for bank in BATTERY_BANKS]))


def recursively(bank, numLeft):
    for i in range (9, 0, -1):
        right = str(i).join(bank.split(str(i))[1:])
        if right == bank:
            continue
        if len(right) >= numLeft-1:
            if numLeft <= 2:
                for z in  range (9, 0, -1):
                    if str(z) in right:
                        return i, z
            else:
                return i, recursively(right, numLeft-1)

def turnOnBatteries(bank, count):
    result = recursively(bank, count)
    joules = 0
    while isinstance(result, tuple):
        joules *= 10
        joules += result[0]
        result = result[1]
    joules *= 10
    joules += result
    return joules

print("joules with twelve batteries per bank:", sum([turnOnBatteries(bank, 12) for bank in BATTERY_BANKS]))
