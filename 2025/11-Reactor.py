#!/usr/bin/env python3
# Copyright (C) 2025 Joe Baker (JoeBlakeB)
# Advent of Code 2025 - Day 11: Reactor
# Usage:
#     python 2025/11-Reactor.py < 2025/inputs/11.txt

import sys

INPUT = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))
NODES = {n.split(": ")[0]: n.split(": ")[1].split(" ") for n in INPUT}

def getRoutesTo(current: str, dest: str, remainingNodes: dict[str, list[str]], requiredRemaining: list[str] = []) -> int:
    if current == dest:
        return not requiredRemaining
    if current not in remainingNodes:
        return 0
    return sum([getRoutesTo(next,
                            dest,
                            {r: rv for r, rv in remainingNodes.items() if r != current},
                            [a for a in requiredRemaining if a != current]
                ) for next in remainingNodes[current]])

print(getRoutesTo("you", "out", NODES))
print(getRoutesTo("svr", "out", NODES, ["fft", "dac"]))