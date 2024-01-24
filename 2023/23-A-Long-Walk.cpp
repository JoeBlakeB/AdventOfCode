// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2023 - Day 23: A Long Walk
// Usage:
//     scripts/cppRun.sh 2023/23-A-Long-Walk.cpp < 2023/inputs/23.txt

#include <iostream>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

struct NextCoordinate { int distance; bool uphill; };
typedef unordered_map<Coordinate, unordered_map<Coordinate, NextCoordinate>> Graph;

Graph buildGraph(const CharGrid& textForest, Coordinate start, Coordinate end) {
    Graph graph;
    queue<pair<Coordinate, Direction>> queue;
    queue.push({start, DOWN});
    unordered_set<Coordinate> visited;

    while (!queue.empty()) {
        auto [nodeStart, direction] = queue.front();
        queue.pop();

        Coordinate current = nodeStart(direction);
        int distance = 0;
        bool uphill = false;

        // Get to the end of this path
        char validNeighborsCount = 1;
        while (validNeighborsCount == 1) {
            distance++;
            validNeighborsCount = 0;
            Direction nextStepDirection = direction;

            if ((textForest[current] == '>' && direction == LEFT) ||
                (textForest[current] == 'v' && direction == UP)) {
                uphill = true;
            }

            for (short i = 0; i < 4; i++) {
                if ((i - direction + 2) % 4 == 0) {
                    continue;
                }

                char neighborValue = textForest[current(Direction(i))];
                if (neighborValue == '#') {
                    continue;
                }

                validNeighborsCount++;
                nextStepDirection = Direction(i);
            }

            if (validNeighborsCount == 1) {
                current = current(nextStepDirection);
                if (current == end) {
                    distance += direction != nextStepDirection;
                    break;
                }
                direction = nextStepDirection;
            }
        }

        bool alreadyReachedJunction = visited.find(current) != visited.end();

        // Add the junction to the graph
        graph[nodeStart][current] = {distance, uphill};

        // Add the next paths to the queue
        if (!alreadyReachedJunction && current != end) {
            visited.insert(current);

            for (short i = 0; i < 4; i++) {

                char neighborValue = textForest[current(Direction(i))];
                if (neighborValue == '#') {
                    continue;
                }

                queue.push({current, Direction(i)});
            }
        }
    }

    return graph;
}

template<bool allowedUphill>
int findLongestDistance(const Graph& graph, Coordinate start, Coordinate end) {
    unsigned int longestDistance = 0;
    stack<tuple<Coordinate, vector<Coordinate>, unsigned int>> stack;
    stack.push({start, {start}, 0});

    while (!stack.empty()) {
        auto [current, path, distance] = stack.top();
        stack.pop();

        for (auto [neighbor, nextCoordinate] : graph.at(current)) {
            if (find(path.begin(), path.end(), neighbor) != path.end()) {
                continue;
            }

            unsigned int newDistance = distance + nextCoordinate.distance;

            if (neighbor == end) {
                if (newDistance > longestDistance) {
                    longestDistance = newDistance;
                }
                continue;
            }

            if constexpr (!allowedUphill) {
                if (nextCoordinate.uphill) {
                    continue;
                }
            }

            vector<Coordinate> newPath = path;
            newPath.push_back(neighbor);

            stack.push({neighbor, newPath, newDistance});
        }
    }

    return longestDistance;
}

int main() {
    CharGrid textForest = {cin};
    Coordinate start = {1, 0};
    Coordinate end = {textForest.height - 2, textForest.width - 1};
    Graph forestGraph = buildGraph(textForest, start, end);
    cout << "Longest Downhill Hike: " << findLongestDistance<false>(forestGraph, start, end) << endl;
    cout << "Longest Climbing Hike: " << findLongestDistance<true>(forestGraph, start, end) << endl;
    return 0;
}
