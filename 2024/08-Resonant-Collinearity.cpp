// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 8: Resonant Collinearity
// Usage:
//     scripts/cppRun.sh 2024/08-Resonant-Collinearity.cpp < 2024/inputs/08.txt

#include <iostream>
#include <queue>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

template <bool resonantHarmonics>
int countAntinodes(const CharGrid& antennaMap) {
    vector<Coordinate> antinodes;

    antennaMap.forEach([&antennaMap, &antinodes](Coordinate antennaA) {
        if (antennaMap[antennaA] == '.') {
            return;
        }

        antennaMap.forEach([&antennaMap, &antinodes, &antennaA](Coordinate antennaB) {
            if (antennaA == antennaB || antennaMap[antennaA] != antennaMap[antennaB]) {
                return;
            }

            Coordinate diff = antennaA - antennaB;

            if constexpr(resonantHarmonics) {
                Coordinate antinode = antennaA;

                while (antennaMap.contains(antinode)) {
                    if (find(antinodes.begin(), antinodes.end(), antinode) == antinodes.end()) {
                        antinodes.push_back(antinode);
                    }
                    antinode += diff;
                }
            } else {
                Coordinate antinode = antennaA + diff;

                if (antennaMap.contains(antinode) && find(antinodes.begin(), antinodes.end(), antinode) == antinodes.end()) {
                    antinodes.push_back(antinode);
                }
            }
        });
    });

    return antinodes.size();
}

int main() {
    const CharGrid antennaMap = {cin};

    cout << "Unique Antinode Locations: " << countAntinodes<false>(antennaMap) << endl;
    cout << "  with Resonant Harmonics: " << countAntinodes<true>(antennaMap) << endl;

    return 0;
}
