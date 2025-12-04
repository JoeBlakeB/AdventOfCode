// Copyright (C) 2025 Joe Baker (JoeBlakeB)
// Advent of Code 2025 - Day 4: Printing Department
// Usage:
//     scripts/cppRun.sh 2025/04-Printing-Department.cpp < 2025/inputs/04.txt

#include <iostream>
#include <string>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

int forkliftRemoveRollsOfPaper(CharGrid& printingDepartment) {
    int accessibleByForklift = 0;
    CharGrid printingDepartmentAfter = printingDepartment;

    printingDepartment.forEach([&printingDepartment, &printingDepartmentAfter, &accessibleByForklift](Coordinate position) {
        if (printingDepartment[position] != '@') {
            return;
        }

        vector<char> neighbors = printingDepartment.neighborValues(position, true);
        int adjacentPaperRolls = std::count_if(neighbors.begin(), neighbors.end(), [](char x) { return x == '@'; });

        if (adjacentPaperRolls < 4) {
            printingDepartmentAfter[position] = ' ';
            accessibleByForklift++;
        }
    });

    printingDepartment = printingDepartmentAfter;
    return accessibleByForklift;
}

int main() {
    CharGrid printingDepartment = {cin};
    int accessibleByForklift = forkliftRemoveRollsOfPaper(printingDepartment);
    cout << "accessible rolls of paper: " << accessibleByForklift << endl;

    int totalRemoved = accessibleByForklift;
    do {
        accessibleByForklift = forkliftRemoveRollsOfPaper(printingDepartment);
        totalRemoved += accessibleByForklift;
    } while (accessibleByForklift != 0);

    cout << "total that can be removed: " << totalRemoved << endl;
    return 0;
}