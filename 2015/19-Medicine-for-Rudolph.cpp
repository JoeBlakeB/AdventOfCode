#include <algorithm>
#include <iostream>
#include <vector>

#include "utils.cpp"

using namespace std;

struct Replacement {
    string from;
    string to;
};

vector<Replacement> getPossibleReplacements() {
    vector<string> inputLines = getInputLinesVector();
    vector<Replacement> possibleReplacements;

    for (string line : inputLines) {
        unsigned short arrowPosition = line.find("=>");
        possibleReplacements.push_back({
            line.substr(0, arrowPosition - 1),
            line.substr(arrowPosition + 3)});
    }

    return possibleReplacements;
}

int getPossibleReplacementCount(
    const string& molecule,
    vector<Replacement>& possibleReplacements
) {
    unsigned int possibleChanges = 0;
    vector<string> otherMolecules;

    for (unsigned int i = 0; i < molecule.size(); i++) {
        string thisAtom = "";
        unsigned short atomSize = 1;
        for (; atomSize <= 2; atomSize++)
        {
            string atomToFind = molecule.substr(i, atomSize);
            if (find_if(possibleReplacements.begin(), possibleReplacements.end(),
                    [&](const Replacement& replacement) {
                        return replacement.from == atomToFind;
                    }) != possibleReplacements.end()) {
                thisAtom = molecule.substr(i, atomSize);
                break;
            }
        }
        if (thisAtom == "") continue;
        
        for (const Replacement& replacement : possibleReplacements) {
            if (replacement.from != thisAtom) continue;

            string newMolecule = molecule.substr(0, i) +
                replacement.to + molecule.substr(i+atomSize);

            if (find(otherMolecules.begin(), otherMolecules.end(), newMolecule)
                    == otherMolecules.end()) {
                possibleChanges++;
                otherMolecules.push_back(newMolecule);
            }
        }
    }

    return possibleChanges;
}

int stepsToGetE(
    const string& fromMolecule,
    vector<Replacement>& possibleReplacements
) {
    string molecule = fromMolecule;
    unsigned int steps = 0;
    for (unsigned int i = 0; i < 1024; i++) {
        for (const Replacement& replacement : possibleReplacements) {
            size_t position = molecule.find(replacement.to);
            if (position == string::npos) continue;
            
            molecule.replace(position, replacement.to.size(), replacement.from);
            steps++;
        }
        if (molecule == "e") return steps;
    }
    cout << "Error: no solution found after 1024 iterations" << endl;
    exit(1);
}

int main() {
    vector<Replacement> reactions = getPossibleReplacements();
    string medicineMolecule = getInputLinesVector()[0];

    cout << "Number of possible distinct molecules: "
         << getPossibleReplacementCount(medicineMolecule, reactions) << endl;

    cout << "Steps to create the medicine molecule: "
         << stepsToGetE(medicineMolecule, reactions) << endl;

    return 0;
}