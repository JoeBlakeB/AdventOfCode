#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

#include "utils.cpp"

using namespace std;

/*
 * For the input, have the MFCSAM ticker tape first, 
 * then a blank line, and then the puzzles input after.
 */

map<string, unsigned int> getTickerTape() {
    map<string, unsigned int> tickerTape;

    for (string line : getInputLinesVector()) {
        tickerTape[
            line.substr(0, line.size() - 3)
        ] = stoi(line.substr(line.size() - 2));
    }

    return tickerTape;
}

class Sue {
public:
    Sue(string data) {
        istringstream iss(data);
        string word1, word2;
        iss >> word2 >> word1;
        id = stoi(word1.substr(0, word1.size() - 1));

        for (unsigned int i = 0; i < 3; i++) {
            iss >> word1 >> word2;
            information.push_back({
                word1.substr(0, word1.size() - 1),
                stoi(i == 2 ? word2 : word2.substr(word2.size() - 2))
            });
        }
    }

    unsigned int getID() { return id; }

    bool isThisYou(map<string, unsigned int>& tickerTape) {
        for (pair<string, unsigned int> info : information) {
            if (tickerTape[info.first] != info.second) {
                return false;
            }
        }
        return true;
    }

    bool isThisYouV2(map<string, unsigned int>& tickerTape) {
        for (pair<string, unsigned int> info : information) {
            if (info.first == "cats" || info.first == "trees") {
                if (tickerTape[info.first] >= info.second) {
                    return false;
                }
            } else if (info.first == "pomeranians" || info.first == "goldfish") {
                if (tickerTape[info.first] <= info.second) {
                    return false;
                }
            } else {
                if (tickerTape[info.first] != info.second) {
                    return false;
                }
            }
        }
        return true;
    }
private:
    unsigned int id;
    vector<pair<string, unsigned int>> information;
};

vector<Sue> getSues() {
    vector<string> sues = getInputLinesVector();
    return vector<Sue> (sues.begin(), sues.end());;
}

int main() {
    map<string, unsigned int> tickerTape = getTickerTape();
    vector<Sue> sues = getSues();

    for (Sue& sue : sues) {
        if (sue.isThisYou(tickerTape)) {
            cout << "The MFCSAM detected sue " << sue.getID() << " in part one" << endl;
        }
    }

    for (Sue& sue : sues) {
        if (sue.isThisYouV2(tickerTape)) {
            cout << "The MFCSAM detected sue " << sue.getID() << " in part two" << endl;
        }
    }

    return 0;
}