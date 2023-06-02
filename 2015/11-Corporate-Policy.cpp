#include <iostream>

using namespace std;

void incrementPassword(string &password) {
    uint i = password.size() - 1;
    password[i] += 1;
    while (password[i] == '{') {
        password[i--] = 'a';
        password[i] += 1;
    }
}

bool passwordContainsIncreasingStraight(string &password) {
    for (ushort i = 0; i < password.size() - 2; ++i) {
        if (password[i] + 1 == password[i + 1] &&
            password[i] + 2 == password[i + 2])
            return true;
    }
    return false;
}

bool passwordDoesntContainConfusingLetters(string &password) {
    for (ushort i = 0; i < password.size(); ++i) {
        if (password[i] == 'i' || password[i] == 'o' || password[i] == 'l')
            return false;
    }
    return true;
}

bool passwordContainsTwoPairs(string &password) {
    ushort pairCount = 0;
    for (ushort i = 1; i < password.size(); ++i) {
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