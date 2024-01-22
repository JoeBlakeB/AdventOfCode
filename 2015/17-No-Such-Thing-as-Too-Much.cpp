// Copyright (C) 2023 Joe Baker (JoeBlakeB)
// Advent of Code 2015 - Day 17: No Such Thing as Too Much Name
// Usage:
//     scripts/cppRun.sh 2015/17-No-Such-Thing-as-Too-Much-Name.cpp < 2015/inputs/17.txt

#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

constexpr unsigned int LITRES = 150;

vector<unsigned int> getInputNumbersSortedVector() {
    vector<unsigned int> inputNumbers;
    string line;
    while (getline(cin, line)) {
        inputNumbers.push_back(stoi(line));
    }
    sort(inputNumbers.rbegin(), inputNumbers.rend());
    return inputNumbers;
}

pair<unsigned int, unsigned int> getPossibleCombinationCount(
    vector<unsigned int>& containerSizes,
    unsigned int targetSum
) {
    unsigned int totalPossibleCombinations = 0;
    unsigned int currentSum = containerSizes[0];
    stack<unsigned int> countedIndexes;
    countedIndexes.push(0);
    unsigned int i = 0;

    unsigned int lowestNumberOfContainers = 0xffffffff;
    unsigned int lowestNumberOfContainersCount = 0;

    while (!countedIndexes.empty()) {
        unsigned int newSum = currentSum + containerSizes[++i];
        if (newSum == targetSum) {
            totalPossibleCombinations++;

            if (countedIndexes.size() + 1 < lowestNumberOfContainers) {
                lowestNumberOfContainers = countedIndexes.size() + 1;
                lowestNumberOfContainersCount = 1;
            } else if (countedIndexes.size() + 1 == lowestNumberOfContainers) {
                lowestNumberOfContainersCount++;
            }
        } else if (newSum < targetSum && i < containerSizes.size() - 1) {
            countedIndexes.push(i);
            currentSum = newSum;
        }

        if (i >= containerSizes.size() - 1) {
            i = countedIndexes.top();
            countedIndexes.pop();
            currentSum -= containerSizes[i];

            if (currentSum == 0 && i < containerSizes.size() - 2) {
                currentSum = containerSizes[++i];
                countedIndexes.push(i);
            }
        }
    }

    return {totalPossibleCombinations, lowestNumberOfContainersCount};
}

int main() {
    vector<unsigned int> containerSizes = getInputNumbersSortedVector();
    
    pair<int, int> possibleCombinations = getPossibleCombinationCount(containerSizes, LITRES);

    cout << "Total combinations of containers for " << LITRES << " liters: "
         << possibleCombinations.first << endl;

    cout << "Lowest number of containers combinations: "
         << possibleCombinations.second << endl;

    return 0;
}