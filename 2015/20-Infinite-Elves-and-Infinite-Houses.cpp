// Copyright (C) 2023 Joe Baker (JoeBlakeB)
// Advent of Code 2015 - Day 20: Infinite Elves and Infinite Houses
// Usage:
//     scripts/cppRun.sh 2015/20-Infinite-Elves-and-Infinite-Houses.cpp < 2015/inputs/20.txt

#include <iostream>

using namespace std;

constexpr int HOUSENUMBER_INCREASE_PER_ITERATION = 720;

unsigned int getInputNumber() {
    string line;
    cin >> line;
    return stoi(line);
}

unsigned int getLowestHouseNumber(unsigned int presentsNeeded) {
    unsigned int houseNumber = HOUSENUMBER_INCREASE_PER_ITERATION;
    unsigned int presentCount;
    do {
        houseNumber += 720;
        presentCount = 0;
        for (unsigned int i = 1; i <= houseNumber; i++) {
            if (houseNumber % i == 0) {
                presentCount += i * 10;
            }
        }
    } while (presentCount < presentsNeeded);
    return houseNumber;
}

unsigned int onlyLastFiftyElves(unsigned int presentsNeeded, unsigned int houseNumber) {
    unsigned int presentCount;
    do {
        houseNumber += HOUSENUMBER_INCREASE_PER_ITERATION;
        presentCount = 0;
        for (unsigned int i = 1; i <= houseNumber; i++) {
            if (houseNumber % i == 0 && houseNumber / i < 50) {
                presentCount += i * 11;
            }
        }
    } while (presentCount < presentsNeeded);
    return houseNumber;
}

int main() {
    unsigned int presentsNeeded = getInputNumber();

    cout << "Calculating Part One..." << flush;

    unsigned int lowestHouseNumber = getLowestHouseNumber(presentsNeeded);
    cout << "\rLowest house number for " << presentsNeeded << " presents: "
         << lowestHouseNumber << endl;  
         
    cout << "Calculating Part Two..." << flush;
    
    lowestHouseNumber = onlyLastFiftyElves(presentsNeeded, lowestHouseNumber);
    cout << "\rLowest number of houses with only the last 50 elves: "
         << lowestHouseNumber << endl;  

    return 0;
}