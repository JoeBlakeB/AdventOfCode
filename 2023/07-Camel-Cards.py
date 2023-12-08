#!/usr/bin/env python3

# Advent of Code 2023 - Day 7: Camel Cards
# Usage:
#     python 2023/07-Camel-Cards.py < 2023/inputs/07.txt

import fileinput
inputSplit = [line.strip() for line in list(fileinput.input())]

ALL_CARDS = "23456789TJQKA"
ALL_CARDS_V2 = "J23456789TQKA"

def getCountsOfEachCard(hand: str) -> dict[str, int]:
    counts = dict()
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return counts

def getCountsOfEachCardV2(hand: str) -> dict[str, int]:
    counts = dict()
    jokers = 0
    for card in hand:
        if card == "J": jokers += 1
        else:
            counts[card] = counts.get(card, 0) + 1
    
    if jokers > 0:
        if counts:
            highestCardCount = max(counts.values())
            cardsWithHighestCount = [card for card, count in counts.items() if count == highestCardCount]
            if len(cardsWithHighestCount) == 1:
                cardToIncrease = cardsWithHighestCount[0]
            else:
                cardToIncrease = max(cardsWithHighestCount, key=lambda card: ALL_CARDS_V2.index(card))
            counts[cardToIncrease] += jokers
        else:
            counts[ALL_CARDS_V2[0]] = jokers
    
    return counts

def getHandType(countsOfEachCard: dict[str, int]) -> int:
    if len(countsOfEachCard) == 1:
        return 6 # Five of a kind
    elif any([count == 4 for count in countsOfEachCard.values()]): # Four of a kind
        return 5
    elif len(countsOfEachCard) == 2:
        return 4 # Full House
    elif any([count == 3 for count in countsOfEachCard.values()]): # Three of a kind
        return 3
    else: # Two and One Pair, High card
        return 5 - len(countsOfEachCard)

def getHandTypeAndIndexes(hand: str) -> tuple[tuple[int, list], tuple[int, list]]:
    handType = getHandType(getCountsOfEachCard(hand))
    handTypeV2 = getHandType(getCountsOfEachCardV2(hand))

    part1 = handType, [ALL_CARDS.index(card) for card in hand]
    part2 = handTypeV2, [ALL_CARDS_V2.index(card) for card in hand]
    return part1, part2

part1Hands = []
part2Hands = []
for line in inputSplit:
    hand, bid = line.split(" ")
    part1, part2 = getHandTypeAndIndexes(hand)
    part1Hands.append((part1, hand, int(bid)))
    part2Hands.append((part2, hand, int(bid)))

part1Hands.sort()
part2Hands.sort()

def getTotalWinnings(hands: list[tuple[tuple[int, list], str, int]]):
    totalWinnings = 0
    for rank, (typeAndIndex, hand, bid) in enumerate(hands, 1):
        totalWinnings += bid * rank
    
    return totalWinnings

print("Total Winnings:", getTotalWinnings(part1Hands))
print("With New Joker Rules:", getTotalWinnings(part2Hands))

