#include <iostream>
#include <string>

using namespace std;

string lookAndSay(string look) {
    string say = "";
    char currentDigit = look[0];
    unsigned int digitCount = 1;
    for (unsigned int i = 1; i < look.size(); ++i) {
        if (look[i] != currentDigit) {
            say += to_string(digitCount) + currentDigit;
            currentDigit = look[i];
            digitCount = 1;
        } else {
            ++digitCount;
        }
    }
    say += to_string(digitCount) + currentDigit;
    return say;
}

int main() {
    string sequence;
    cin >> sequence;

    for (unsigned int i = 0; i < 40; ++i)
        sequence = lookAndSay(sequence);
    cout << "40 times: " << sequence.size() << endl;

    for (unsigned int i = 0; i < 10; ++i)
        sequence = lookAndSay(sequence);
    cout << "50 times: " << sequence.size() << endl;

    return 0;
}