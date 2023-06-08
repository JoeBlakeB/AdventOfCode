#include <iostream>
#include <vector>

using namespace std;

int countAllNumbers(string data) {
    int sum = 0;
    bool isNumber = false;
    string currentNumber = "";
    for (char character : data) {
        if (isdigit(character) || (character == '-' && !isNumber)) {
            isNumber = true;
            currentNumber += character;
        } else if (isNumber) {
            isNumber = false;
            sum += stoi(currentNumber);
            currentNumber = "";
        }
    }
    return sum;
}

struct Depth {
    bool object;
    bool ignore = false;
    int sum = 0;
};

int countAllNumbersIgnoreRed(string data) {
    int sum = 0;
    bool isNumber = false;
    string currentNumber = "";

    vector<Depth> levels;

    for (uint i = 0; i < data.size(); ++i) {
        char character = data[i];

        if (character == '{' || character == '[') {
            levels.push_back(Depth{character == '{'});
        }

        if (isdigit(character) || (character == '-' && !isNumber)) {
            isNumber = true;
            currentNumber += character;
        } else if (isNumber) {
            isNumber = false;
            levels.back().sum += stoi(currentNumber);
            currentNumber = "";
        } else if (levels.back().object && character == 'r' &&
                   data[i + 1] == 'e' && data[i + 2] == 'd') {
            levels.back().ignore = true;
        }

        if (character == '}' || character == ']') {
            int levelsSum = 0;
            if (!levels.back().ignore) {
                levelsSum += levels.back().sum;
            }
            levels.pop_back();

            if (levels.empty()) {
                sum += levelsSum;
            } else {
                levels.back().sum += levelsSum;
            }
        }
    }
    return sum;
}

int main() {
    string json;
    cin >> json;

    cout << "Sum of all numbers: " << countAllNumbers(json) << endl;
    cout << "Ignoring objects with \"red\": " << countAllNumbersIgnoreRed(json) << endl;

    return 0;
}