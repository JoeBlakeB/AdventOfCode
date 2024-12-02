// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 2: Red-Nosed Reports
// Usage:
//     scripts/cppRun.sh 2024/02-Red-Nosed-Reports.cpp < 2024/inputs/02.txt

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> getReports() {
    vector<vector<int>> reports;
    string line;
    
    while (getline(std::cin, line) && line != "") {
        vector<int> report;
        istringstream iss(line);
        string number;

        while (!iss.eof()) {
            iss >> number;
            report.push_back(stoi(number));
        }

        reports.push_back(report);
    }

    return reports;
}

constexpr int MAX_SAFETY = 3;

bool areNumbersSafe(int num1, int num2, bool goingUp) {
    return ((num1 < num2) != goingUp) ||
        (abs(num1 - num2) > MAX_SAFETY) ||
        (num1 == num2);
}

bool isReportSafe(vector<int> report) {
    bool goingUp = report[0] < report[1];

    for (size_t i = 0; i < report.size()-1; i++) {
        if (
            ((report[i] < report[i+1]) != goingUp) +
            (abs(report[i] - report[i+1]) > MAX_SAFETY) +
            (report[i] == report[i+1])
        ) {
            return false;
        }

        goingUp = report[i] < report[i+1];
    }

    return true;
}

int countSafeReports(vector<vector<int>> reports) {
    int safeReportCount = 0;
    for (size_t i = 0; i < reports.size(); i++) {
        safeReportCount += isReportSafe(reports[i]);
    }
    return safeReportCount;
}

int countSafeReportsWithProblemDampener(vector<vector<int>> reports) {
    int safeReportCount = 0;
    for (size_t i = 0; i < reports.size(); i++) {
        if (isReportSafe(reports[i])) {
            safeReportCount++;
        } else {
            for (size_t j = 0; j < reports[i].size(); ++j) {
                vector<int> modified;
                for (size_t k = 0; k < reports[i].size(); ++k) {
                    if (k != j) {
                        modified.push_back(reports[i][k]);
                    }
                }

                if (isReportSafe(modified)) {
                    safeReportCount++;
                    break;
                }
            }
        }
    }
    return safeReportCount;
}

int main() {
    vector<vector<int>> reports = getReports();

    cout << "there are " << countSafeReports(reports) << " safe reports" << endl;
    cout << "there are " << countSafeReportsWithProblemDampener(reports) << " safe reports with the problem dampener activated" << endl;

    return 0;
}