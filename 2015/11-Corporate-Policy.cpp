// Copyright (C) 2023 Joe Baker (JoeBlakeB)
// Advent of Code 2015 - Day 11: Corporate Policy
// Usage:
//     scripts/cppRun.sh 2015/11-Corporate-Policy.cpp < 2015/inputs/11.txt

#include <iostream>

using namespace std;

void incrementPassword(string &password) {
    unsigned int i = password.size() - 1;
    password[i] += 1;
    while (password[i] == '{') {
        password[i--] = 'a';
        password[i] += 1;
    }
}

bool passwordContainsIncreasingStraight(string &password) {
    for (unsigned short i = 0; i < password.size() - 2; ++i) {
        if (password[i] + 1 == password[i + 1] &&
            password[i] + 2 == password[i + 2])
            return true;
    }
    return false;
}

bool passwordDoesntContainConfusingLetters(string &password) {
    for (unsigned short i = 0; i < password.size(); ++i) {
        if (password[i] == 'i' || password[i] == 'o' || password[i] == 'l')
            return false;
    }
    return true;
}

bool passwordContainsTwoPairs(string &password) {
    unsigned short pairCount = 0;
    for (unsigned short i = 1; i < password.size(); ++i) {
        if (password[i-1] == password[i]) {
            ++pairCount;
            ++i;
        }
    }
    return pairCount >= 2;
}

bool isPasswordValid(string &password) {
    return passwordContainsIncreasingStraight(password) &&
           passwordDoesntContainConfusingLetters(password) &&
           passwordContainsTwoPairs(password);
}

int main() {
    string password;
    cin >> password;

    do incrementPassword(password);
    while (!isPasswordValid(password));

    cout << password << endl;

    return 0;
}