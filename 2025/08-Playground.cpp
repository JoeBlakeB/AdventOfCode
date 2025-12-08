// Copyright (C) 2025 Joe Baker (JoeBlakeB)
// Advent of Code 2025 - Day 8: Playground
// Usage:
//     scripts/cppRun.sh 2025/08-Playground.cpp < 2025/inputs/08.txt

#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

struct Junction {
    int x, y, z;
    vector<Junction*> connections;

    double distance(Junction other) {
        return sqrt(pow(abs(x - other.x), 2) + pow(abs(y - other.y), 2) + pow(abs(z - other.z), 2));
    }

    string toString() {
        return "(" + to_string(x) + ", " + to_string(y) + ", " + to_string(z) + ")";
    }
};

vector<Junction> getJunctions() {
    vector<Junction> junctions;
    string line;
    while (getline(cin, line) && line != "") {
        int x, y, z;
        sscanf(line.c_str(), "%d,%d,%d", &x, &y, &z);
        junctions.push_back({x, y, z, {}});
    }
    return junctions;
}

vector<pair<double, pair<Junction*, Junction*>>> calculateDistances(vector<Junction>& junctions) {
    vector<pair<double, pair<Junction*, Junction*>>> connections = {};

    for (size_t a = 0; a < junctions.size(); a++) {
        for (size_t b = a + 1; b < junctions.size(); b++) {
            double dist = junctions[a].distance(junctions[b]);
            connections.push_back({dist, {&junctions[a], &junctions[b]}});
        }
    }

    std::sort(connections.begin(), connections.end());
    return connections;
}

vector<int> getCircuitSizes(vector<Junction>& junctions) {
    vector<Junction*> junctionsInACircuit = {};
    vector<int> circuitSizes = {};

    for (size_t i = 0; i < junctions.size(); i++) {
        Junction* thisJunction = &junctions[i];
        if (find(junctionsInACircuit.begin(), junctionsInACircuit.end(), thisJunction) != junctionsInACircuit.end()) continue;
        int thisCircuitSize = 0;
        queue<Junction*> q;
        q.push(thisJunction);

        while (!q.empty()) {
            Junction* nextJunction = q.front();
            q.pop();
            if (find(junctionsInACircuit.begin(), junctionsInACircuit.end(), nextJunction) != junctionsInACircuit.end()) continue;
            junctionsInACircuit.push_back(nextJunction);
            thisCircuitSize++;
            for (Junction* nextnext : nextJunction->connections) {
                q.push(nextnext);
            }
        }

        circuitSizes.push_back(thisCircuitSize);
    }

    return circuitSizes;
}

pair<Junction*, Junction*> makeNextConnection(vector<pair<double, pair<Junction*, Junction*>>>& distances) {
    Junction* a = nullptr;
    Junction* b = nullptr;

    while (!distances.empty()) {
        a = distances[0].second.first;
        b = distances[0].second.second;
        distances.erase(distances.begin());
        if (find(a->connections.begin(), a->connections.end(), b) != a->connections.end() ||
            find(b->connections.begin(), b->connections.end(), a) != b->connections.end()) {
                continue;
        };
        a->connections.push_back(b);
        b->connections.push_back(a);
        break;
    }

    return {a, b};
}

int main() {
    vector<Junction> junctions = getJunctions();
    auto distances = calculateDistances(junctions);
    int amountToConnect = junctions.size() > 20 ? 1000 : 10;

    for (int i = 0; i < amountToConnect; i++) {
        makeNextConnection(distances);
    }

    vector<int> circuitSizes = getCircuitSizes(junctions);
    sort(circuitSizes.begin(), circuitSizes.end(), greater<int>());
    long long prod = 1;

    for (int i = 0; i < 3 && i < (int)circuitSizes.size(); i++) {
        prod *= circuitSizes[i];
    }

    cout << "three largest circuits: " << prod << endl;

    pair<Junction*, Junction*> finalJunctions = {nullptr, nullptr};

    while (getCircuitSizes(junctions).size() > 1) {
        finalJunctions = makeNextConnection(distances);
    }

    if (finalJunctions.first != nullptr && finalJunctions.second != nullptr) {
        cout << "multiplied X on final connection: " << (finalJunctions.first->x * finalJunctions.second->x) << endl;
    }

    return 0;
}
