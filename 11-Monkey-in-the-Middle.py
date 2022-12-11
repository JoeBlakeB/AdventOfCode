#!/usr/bin/env python3

# Day 11: Monkey in the Middle

class Monkey:
    inspections = 0

    def __init__(self, monkeys, data):
        self.otherMonkeys = monkeys
        data = data.split("\n")
        self.items = [int(item) for item in data[1].split("Starting items: ")[1].split(", ")]
        exec("self.operation = lambda old: " + data[2].split("Operation: ")[1][6:])
        self.test = int(data[3].split("divisible by ")[1])
        self.throw = [
            int(data[4].split("true: throw to monkey ")[1]),
            int(data[5].split("false: throw to monkey ")[1])]

    def __repr__(self):
        return str(self.inspections)

    def __lt__(self, otherMonkey):
        return self.inspections < otherMonkey.inspections

    def doRound(self):
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operation(item)
            if worryModulo:
                item = item % worryModulo
            else:
                item = int(item / 3)
            self.otherMonkeys[
                self.throw[int(bool(item % self.test))]
            ].items.append(item)

with open("inputs/11.txt") as f:
    data = f.read().split("\n\n")

for numberOfRounds, worryModulo in (20, False), (10000, True):
    monkeys = []
    for monkeyData in data:
        monkeys.append(Monkey(monkeys, monkeyData))

    if worryModulo:
        worryModulo = 1
        for monkey in monkeys:
            worryModulo *= monkey.test

    for round in range(numberOfRounds):
        for monkey in monkeys:
            monkey.doRound()

    monkeys.sort()
    monkeyBusiness = monkeys[-1].inspections * monkeys[-2].inspections
    print(f"Monkey Business after {numberOfRounds} rounds of Simian Shenanigans: {monkeyBusiness}")
