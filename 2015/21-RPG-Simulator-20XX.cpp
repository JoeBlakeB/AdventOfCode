// Copyright (C) 2023 Joe Baker (JoeBlakeB)
// Advent of Code 2015 - Day 21: RPG Simulator 20XX
// Usage:
//     scripts/cppRun.sh 2015/21-RPG-Simulator-20XX.cpp < 2015/inputs/21.txt

#include <array>
#include <climits>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "utils.cpp"

using namespace std;

/*
 * For the input, have the three paragraphs for the shops selling
 * and a paragraph for boss's stats in the input with one empty line between.
 */

struct Item {
    string name;
    const int cost, damage, armor;
};

class Character {
public:
    int hitPoints, damage, armor;

    Character(int hitPoints, int damage, int armor)
        : hitPoints(hitPoints), damage(damage), armor(armor) {}

    Character(vector<string> input) : Character(
        stoi(input[0].substr(12)),
        stoi(input[1].substr(8)),
        stoi(input[2].substr(7))
    ) {}

    bool operator>(const Character& enemyOriginal) const {
        Character me = *this;
        Character enemy = enemyOriginal;
        unsigned int currentTurn = 0;

        for (; me.hitPoints > 0 && enemy.hitPoints > 0; currentTurn = (currentTurn + 1) % 2) {
            Character& attacker = currentTurn == 0 ? me : enemy;
            Character& defender = currentTurn == 0 ? enemy : me;

            int attackDamage = attacker.damage - defender.armor;
            if (attackDamage < 1) attackDamage = 1;
            defender.hitPoints -= attackDamage;
        }
        
        return me.hitPoints > 0;
    }
};

vector<Item> getItemSet(vector<string> input) {
    vector<Item> items;
    for (size_t i = 1; i < input.size(); i++) {
        istringstream iss(input[i]);
        string name;
        int values [3];

        for (int j = 0; j < 3;) {
            string word;
            iss >> word;
            if (isdigit(word[0])) {
                values[j++] = stoi(word);
            } else {
                name += word;
            }
        }
        
        items.push_back(
            Item({name, values[0], values[1], values[2]})
        );
    }
    return items;
}

int main() {
    vector<Item> weapons = getItemSet(getInputLinesVector());
    vector<Item> armorSets = getItemSet(getInputLinesVector());
    vector<Item> rings = getItemSet(getInputLinesVector());
    Character boss(getInputLinesVector());

    armorSets.push_back(Item({"None", 0, 0, 0}));
    rings.push_back(Item({"None", 0, 0, 0}));

    int lowestCost = INT_MAX;
    int highestCost = INT_MIN;
    array<string, 4> lowestCostItems;
    array<string, 4> highestCostItems;

    for (Item& weapon : weapons) {
        for (Item& armor : armorSets) {
            for (int r1 = rings.size()-1; r1 >= 0; r1--) {
                int r2 = rings.size()-1;
                do {
                    
                    int cost = weapon.cost + armor.cost + rings[r1].cost + rings[r2].cost;
                    if (cost < lowestCost || cost > highestCost) {
                        Character player(100,
                            weapon.damage + rings[r1].damage + rings[r2].damage,
                            armor.armor + rings[r1].armor + rings[r2].armor);
                        if (player > boss && cost < lowestCost) {
                            lowestCost = cost;
                            lowestCostItems = {weapon.name, armor.name,
                                            rings[r1].name, rings[r2].name};
                        }
                        if (!(player > boss) && cost > highestCost) {
                            highestCost = cost;
                            highestCostItems = {weapon.name, armor.name,
                                            rings[r1].name, rings[r2].name};
                        }
                    }

                } while (--r2 > r1);
            }
        }
    }

    cout << "The least amounts of gold you can spend to win is: "
         << lowestCost << endl;
    cout << "With: " << lowestCostItems[0] << ", " << lowestCostItems[1] << ", " 
         << lowestCostItems[2] << ", " << lowestCostItems[3] << "\n" << endl;

    cout << "The most amounts of gold you can spend but still lose is: "
         << highestCost << endl;
    cout << "With: " << highestCostItems[0] << ", " << highestCostItems[1] << ", "
         << highestCostItems[2] << ", " << highestCostItems[3] << endl;

    return 0;
}