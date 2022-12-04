#!/usr/bin/env python3

# Day 2: Rock Paper Scissors

with open("inputs/02.txt") as f:
    data = f.read().strip()

score1 = 0
score2 = 0
pointsForChoice = {"X": 1, "Y": 2, "Z": 3}
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Z", "B": "X", "C": "Y"}
task2 = {"Z": (win, 6), "Y": (draw, 3), "X": (lose, 0)}

for game in data.split("\n"):
    opponent, player = game.split(" ")
    # Task 1
    score1 += pointsForChoice[player]
    if player == win[opponent]:
        score1 += 6
    elif player == draw[opponent]:
        score1 += 3
    # Task 2
    score2 += pointsForChoice[task2[player][0][opponent]] + task2[player][1]

print("Task 1", score1)
print("Task 2", score2)
