#!/usr/bin/env python3
# Copyright (C) 2023 Joe Baker (JoeBlakeB)
# Advent of Code 2023 - Day 19: Aplenty
# Usage:
#     python 2023/19-Aplenty.py < 2023/inputs/19.txt

import sys
import re


WORKFLOW_SPECS = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))
PART_RATINGS = list(iter(lambda: next(sys.stdin).rstrip("\n"), ""))

RULE_CHAR = 0
RULE_GREATER_THAN = 1
RULE_COMPARISON_INT = 2
RULE_SEND_PART_TO_NEXT = 3


class Workflow:
    def __init__(self, spec: str, workflows: dict[str, "Workflow"]):
        self.name: str = spec.split("{")[0]
        self.workflows = workflows
        self.workflows[self.name] = self

        rules = spec.split("{")[1][:-1].split(",")
        self.final = rules[-1]
        self.rules: list[tuple[str, bool, int, str]] = [(
                rule[0], # XMAS char
                rule[1] == ">", # is greater than
                int(rule[2:].split(":")[0]), # comparison score
                rule.split(":")[1] # send part to next
            ) for rule in rules[:-1]]
        
    def __repr__(self) -> str:
        return (f"{self.name}{{" +
            ",".join([f"{rule[RULE_CHAR]}{'>' if rule[RULE_GREATER_THAN] else '<'}{rule[RULE_COMPARISON_INT]}:{rule[RULE_SEND_PART_TO_NEXT]}"
                for rule in self.rules]) +
            f",{self.final}}}")

    def __call__(self, part: dict[str, int]) -> bool:
        for rule in self.rules:
            if (part[rule[RULE_CHAR]] > rule[RULE_COMPARISON_INT]) == rule[RULE_GREATER_THAN]:
                return self.evaluate(part, rule[RULE_SEND_PART_TO_NEXT])

        return self.evaluate(part, self.final)
    
    def evaluate(self, part: dict[str, int], function: str) -> bool:
        if function == "A":
            return True
        elif function == "R":
            return False
        else:
            return self.workflows[function](part)
        
    def bulkAccept(self, partRanges: dict[str, range]) -> int:
        amountAccepted = 0

        for rule in self.rules:
            splitPartRanges = partRanges.copy()
            splitPartRanges[rule[RULE_CHAR]] = range(
                rule[RULE_COMPARISON_INT] + rule[RULE_GREATER_THAN],
                partRanges[rule[RULE_CHAR]].stop)
            partRanges[rule[RULE_CHAR]] = range(
                partRanges[rule[RULE_CHAR]].start,
                rule[RULE_COMPARISON_INT] + rule[RULE_GREATER_THAN])

            if not rule[RULE_GREATER_THAN]:
                partRanges, splitPartRanges = splitPartRanges, partRanges

            amountAccepted += self.bulkEvaluate(splitPartRanges, rule[RULE_SEND_PART_TO_NEXT])

        return amountAccepted + self.bulkEvaluate(partRanges, self.final)
    
    def bulkEvaluate(self, partRanges: dict[str, range], function: str) -> int:
        if function == "A":
            return (len(partRanges["x"]) *
                    len(partRanges["m"]) *
                    len(partRanges["a"]) *
                    len(partRanges["s"]))
        elif function == "R":
            return 0
        else:
            return self.workflows[function].bulkAccept(partRanges)


def createPart(partRating: str) -> dict:
    pattern = r'(\w+)=(\d+)'
    matches = re.findall(pattern, partRating)
    return {key: int(value) for key, value in matches}


if __name__ == "__main__":
    workflows: dict[str, "Workflow"] = {}
    for spec in WORKFLOW_SPECS:
        Workflow(spec, workflows)
    isAccepted = workflows["in"]
    
    parts = [createPart(p) for p in PART_RATINGS]
    ratingSum = sum(sum(part.values()) for part in parts if isAccepted(part))
    print("Sum of all accepted parts ratings:", ratingSum)

    partRanges = {"x": range(1, 4001),
                  "m": range(1, 4001),
                  "a": range(1, 4001),
                  "s": range(1, 4001)}
    print("Total possible combinations of accepted parts:", isAccepted.bulkAccept(partRanges))

