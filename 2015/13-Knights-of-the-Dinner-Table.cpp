#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

#include "utils.cpp"

using namespace std;

vector<pair<char, map<char, int>>> getAttendees(vector<string> inputLines) {
    vector<pair<char, map<char, int>>> attendees;
    char currentAttendee = ' ';

    for (string line : inputLines) {
        if (currentAttendee != line[0]) {
            currentAttendee = line[0];
            attendees.push_back({line[0], {}});
        }

        bool isPositive;
        int happiness;

        istringstream iss(line);
        string word;
        iss >> word >> word >> word;
        isPositive = word[0] == 'g';
        iss >> word;
        happiness = stoi(word);
        for (int i = 0; i < 7; i++) { iss >> word; };
        attendees.back().second[word[0]] = isPositive ? happiness : 0 - happiness;
    }

    return attendees;
}

pair<int, int> calculateTotalHappiness(vector<pair<char, map<char, int>>> attendees) {
    pair<int, int> highestTotalHappiness = {INT_MIN, INT_MIN};

    do {
        int totalHappiness = 0;
        int lowestPairHappiness = INT_MAX;

        for (size_t i = 0; i < attendees.size(); i++) {
            int pairHappiness = attendees[i].second[attendees[(i + 1) % attendees.size()].first]
                              + attendees[(i + 1) % attendees.size()].second[attendees[i].first];

            totalHappiness += pairHappiness;
            if (pairHappiness < lowestPairHappiness) {
                lowestPairHappiness = pairHappiness;
            }
        }

        if (totalHappiness > highestTotalHappiness.first) {
            highestTotalHappiness = {totalHappiness, totalHappiness - lowestPairHappiness};
        }
    } while (next_permutation(attendees.begin(), attendees.end()));
    
    return highestTotalHappiness;
}

int main() {
    vector<pair<char, map<char, int>>> attendees = getAttendees(getInputLinesVector());
    
    pair<int, int> totalHappinesses = calculateTotalHappiness(attendees);
    cout << "Total Happiness Part One: " << totalHappinesses.first << endl;
    cout << "                Part Two: " << totalHappinesses.second << endl;

    return 0;
}