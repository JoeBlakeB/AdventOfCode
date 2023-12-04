// Advent of Code 2023 - Day 4: Scratchcards
// Usage:
//     scripts/cppRun.sh 2023/04-Scratchcards.cpp < 2023/inputs/04.txt

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

// Demo
// constexpr int WINNING_NUM_COUNT = 5;
// constexpr int CHOSEN_NUM_COUNT = 8;
// Actual input
constexpr int WINNING_NUM_COUNT = 10;
constexpr int CHOSEN_NUM_COUNT = 25;

typedef pair<int[WINNING_NUM_COUNT], int[CHOSEN_NUM_COUNT]> Scratchcard;

vector<Scratchcard> getScratchcards() {
    vector<Scratchcard> scratchcards;
    string line;
    while (getline(std::cin, line) && line != "") {
        istringstream iss(line);
        string word;
        Scratchcard scratchcard;

        iss >> word;
        iss >> word;

        for (int i = 0; i < WINNING_NUM_COUNT; i++) {
            iss >> word;
            scratchcard.first[i] = stoi(word);
        }

        iss >> word;

        for (int i = 0; i < CHOSEN_NUM_COUNT; i++) {
            iss >> word;
            scratchcard.second[i] = stoi(word);
        }

        scratchcards.push_back(scratchcard);
    }

    return scratchcards;
}

int sumPoints(vector<Scratchcard> scratchcards) {
    int sum = 0;
    for (Scratchcard scratchcard : scratchcards) {
        int matches = 0;
        for (int i = 0; i < WINNING_NUM_COUNT; i++) {
            matches += find(begin(scratchcard.second), end(scratchcard.second),
                            scratchcard.first[i]) != end(scratchcard.second);
        }
        sum += pow(2, matches - 1);
    }
    return sum;
}

int countScratchcards(vector<Scratchcard> scratchcards) {
    int totalScratchcardCount = 0;
    vector<int> scratchcardCounts(scratchcards.size(), 1);
    for (long unsigned int i = 0; i < scratchcards.size(); i++) {
        int amountOfThisScratchcard = scratchcardCounts[i];
        totalScratchcardCount += amountOfThisScratchcard;

        Scratchcard scratchcard = scratchcards[i];
        int matches = 0;
        for (int j = 0; j < WINNING_NUM_COUNT; j++) {
            matches += find(begin(scratchcard.second), end(scratchcard.second),
                            scratchcard.first[j]) != end(scratchcard.second);
        }

        for (long unsigned int j = i + 1; j <= i + matches && j < scratchcards.size(); j++) {
            scratchcardCounts[j] += amountOfThisScratchcard;
        }
    }
    return totalScratchcardCount;
}

int main() {
    vector<Scratchcard> scratchcards = getScratchcards();
    cout << "Sum of points: " << sumPoints(scratchcards) << endl;
    cout << "Total Scratchcards ended up with: " << countScratchcards(scratchcards) << endl;
    return 0;
}
