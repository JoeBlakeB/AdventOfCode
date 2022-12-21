#!/usr/bin/env python3

# Day 21: Monkey Maths

with open("inputs/21.txt") as f:
    data = f.read().strip().split("\n")
    values = {line.split(": ")[0]: line.split(": ")[1] for line in data}

swapOperations = {"+": "-", "-": "+", "*": "/", "/": "*", "==": "=="}

def calculate(value):
    if values[value].isdigit():
        return values[value], [] if value == "humn" else None
    else:
        a = calculate(values[value].split(" ")[0])
        b = calculate(values[value].split(" ")[2])
        human = a[1] if a[1] != None else (b[1] if b[1] != None else None)
        if human != None:
            number = a[0] if b[1] != None else b[0]
            operation = values[value].split(" ")[1]
            if operation in "/-" and b[1] != None:
                human.append(number + operation + "x")
            else:
                oppositeOperation = swapOperations[operation]
                human.append("x" + oppositeOperation + number)
        return (str(eval(
            a[0] + " " + 
            values[value].split(" ")[1] +
            " " + b[0])).split(".")[0],
            human)

a, b = [calculate(v) for v in values["root"].split(" + ")]

print("The value of root is:", int(a[0]) + int(b[0]))

humanSide = a[1] if b[1] == None else b[1]
x = int(a[0] if a[1] == None else b[0])

for operation in humanSide[::-1]:
    x = int(eval(operation))

print("Human number needed for root to be True:", x)
