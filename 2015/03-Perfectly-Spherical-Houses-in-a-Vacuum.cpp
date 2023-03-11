#include <iostream>
#include <map>

int simulate(std::string input, int santaCount) {
    std::map<int, int> counts = {{0, santaCount}};

    int **coords = new int *[santaCount];

    for (int i = 0; i < santaCount; i++) {
        coords[i] = new int[2];
        coords[i][0] = 0;
        coords[i][1] = 0;
    }

    int currentSanta = 0;

    for (long unsigned int i = 0; i < input.length(); i++) {
        switch (input[i]) {
            case '>':
                coords[currentSanta][0]++;
                break;
            case '<':
                coords[currentSanta][0]--;
                break;
            case '^':
                coords[currentSanta][1]++;
                break;
            case 'v':
                coords[currentSanta][1]--;
                break;
        }

        counts[coords[currentSanta][0] * 1000 + coords[currentSanta][1]]++;

        currentSanta = (currentSanta + 1) % santaCount;
    }

    return counts.size();
}

int main() {
    std::string input;
    std::cin >> input;

    std::cout << "Houses with at least one present: " << simulate(input, 1) << std::endl;
    std::cout << "Houses with robot santa helping: " << simulate(input, 2) << std::endl;

    return 0;
}