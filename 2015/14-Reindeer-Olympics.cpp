#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "utils.cpp"

using namespace std;

constexpr int SECONDS = 2503;

class Reindeer {
public:
    string name;
    unsigned int distanceTraveled = 0;
    unsigned int points = 0;

    Reindeer(string& line) {
        string word;
        istringstream iss(line);

        iss >> name >> word >> word >> word;
        speed = stoi(word);
        iss >> word >> word >> word;
        flyDuration = stoi(word);
        for (int i = 0; i < 7; i++) { iss >> word; };
        restSeconds = stoi(word);
    }

    unsigned int runForSeconds(int seconds) {
        return ((seconds / (flyDuration + restSeconds)) * speed * flyDuration)
             + (min(flyDuration, (seconds % (flyDuration + restSeconds))) * speed);
    }

    unsigned int runForOneSecondGetDistance() {
        if (secondsPassed++ < flyDuration) {
            distanceTraveled += speed;
        }
        secondsPassed %= flyDuration + restSeconds;
        return distanceTraveled;
    }

private:
    unsigned int speed, flyDuration, restSeconds;
    unsigned int secondsPassed = 0;
};

vector<Reindeer> getReindeer(vector<string> inputLines) {
    vector<Reindeer> reindeers;

    for (string line : inputLines) {
        reindeers.push_back({line});
    }

    return reindeers;
}

int main() {
    vector<Reindeer> reindeers = getReindeer(getInputLinesVector());

    for (unsigned int i = 0; i < SECONDS; i++) {
        unsigned int furthestDistance = 0;
        for (Reindeer& reindeer : reindeers) {
            furthestDistance = max(furthestDistance, reindeer.runForOneSecondGetDistance());
        }
        for (Reindeer& reindeer : reindeers) {
            if (furthestDistance == reindeer.distanceTraveled) {
                reindeer.points += 1;
            }
        }
    }

    unsigned int highestDistance = 0;
    unsigned int highestPoints = 0;

    for (Reindeer reindeer : reindeers) {
        highestDistance = max(highestDistance, reindeer.runForSeconds(SECONDS));
        highestPoints = max(highestPoints, reindeer.points);
    }

    cout << "Furthest Traveled Reindeer: " << highestDistance << endl;
    cout << "Most Number of Points: " << highestPoints << endl;
    
    return 0;
}
