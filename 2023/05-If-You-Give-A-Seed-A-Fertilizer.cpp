// Advent of Code 2023 - Day 5: If You Give A Seed A Fertilizer
// Usage:
//     scripts/cppRun.sh 2023/05-If-You-Give-A-Seed-A-Fertilizer.cpp < 2023/inputs/05.txt

#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<long long int> getSeeds() {
    string line, word;
    getline(cin, line);
    istringstream iss(line);
    vector<long long int> seeds;
    iss >> word;
    while (!iss.eof()) {
        iss >> word;
        seeds.push_back(stoll(word));
    }
    return seeds;
}

class Mapping {
public:
    long long int rangeStart;
    long long int rangeEnd;
    long long int amountToAdd;

    Mapping(long long int startOfOutput, long long int startOfInput, long long int rangeLength) {
        this->rangeStart = startOfInput;
        this->rangeEnd = startOfInput + rangeLength - 1;
        this->amountToAdd = startOfOutput - startOfInput;
    }
};

vector<vector<Mapping>> getAlminac() {
    vector<vector<Mapping>> alminac;
    string line, words[3];
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    while (cin.peek() != EOF && cin.peek() != '\n') {
        vector<Mapping> mappings;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        while (getline(cin, line) && line != "") {
            istringstream iss(line);
            iss >> words[0] >> words[1] >> words[2];
            mappings.push_back(Mapping(stoll(words[0]), stoll(words[1]), stoll(words[2])));
        }
        alminac.push_back(mappings);
    }
    
    return alminac;
}

long long int getLowestLocationNumber(vector<long long int> seeds, vector<vector<Mapping>> alminac) {
    long long int lowestLocationNumber = numeric_limits<long long int>::max();
    for (long long int seed : seeds) {
        for (vector<Mapping> mappings : alminac) {
            for (Mapping mapping : mappings) {
                if (seed >= mapping.rangeStart && seed <= mapping.rangeEnd) {
                    seed += mapping.amountToAdd;
                    break;
                }
            }
        }
        if (seed < lowestLocationNumber) {
            lowestLocationNumber = seed;
        }
    }
    return lowestLocationNumber;
}

long long int getLowestLocationNumberRanges(vector<long long int> seeds, vector<vector<Mapping>> alminac) {
    vector<pair<long long int, long long int>> seedRanges;
    for (unsigned int i = 0; i < seeds.size(); i+=2) {
        seedRanges.push_back(make_pair(seeds[i], seeds[i] + seeds[i + 1] - 1));
    }

    for (vector<Mapping> mappings : alminac) {
        vector<pair<long long int, long long int>> nextSeedRanges;
        while (seedRanges.size() > 0) {
            pair<long long int, long long int> seedRange = seedRanges.back();
            seedRanges.pop_back();
            bool seedRangeMapped = false;

            for (Mapping mapping : mappings) {
                if (seedRange.second >= mapping.rangeStart && seedRange.first <= mapping.rangeEnd) {
                    long long int firstSeedInMappingRange = max(seedRange.first, mapping.rangeStart);
                    long long int lastSeedInMappingRange = min(seedRange.second, mapping.rangeEnd);

                    if (firstSeedInMappingRange > seedRange.first) {
                        seedRanges.push_back(make_pair(seedRange.first, firstSeedInMappingRange - 1));
                    }
                    if (lastSeedInMappingRange < seedRange.second) {
                        seedRanges.push_back(make_pair(lastSeedInMappingRange + 1, seedRange.second));
                    }
                    nextSeedRanges.push_back(make_pair(firstSeedInMappingRange + mapping.amountToAdd,
                                                      lastSeedInMappingRange + mapping.amountToAdd));
                    
                    seedRangeMapped = true;
                    break;
                }
            }

            if (!seedRangeMapped) {
                nextSeedRanges.push_back(seedRange);
            }
        }
        seedRanges = nextSeedRanges;
    }

    long long int lowestLocationNumber = numeric_limits<long long int>::max();

    for (pair<long long int, long long int> seedRange : seedRanges) {
        if (seedRange.first < lowestLocationNumber) {
            lowestLocationNumber = seedRange.first;
        }
    }

    return lowestLocationNumber;
}

int main() {
    vector<long long int> seeds = getSeeds();
    vector<vector<Mapping>> alminac = getAlminac();
    cout << "Lowest Location As Individual Seeds: " << getLowestLocationNumber(seeds, alminac) << endl;
    cout << "Lowest Location As Ranges of Seeds: " << getLowestLocationNumberRanges(seeds, alminac) << endl;
    return 0;
    
}
