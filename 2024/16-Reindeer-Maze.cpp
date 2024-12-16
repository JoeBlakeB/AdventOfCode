// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2024 - Day 16: Reindeer Maze
// Usage:
//     scripts/cppRun.sh 2024/16-Reindeer-Maze.cpp < 2024/inputs/16.txt

#include <iostream>
#include <limits>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

#include "../Utils/Grid.cpp"

using namespace std;

pair<int, int> findFastestRoute(CharGrid maze, Coordinate start, Coordinate finish) {
    typedef tuple<int, Coordinate, Direction, set<Coordinate>> Reindeer;
    priority_queue<Reindeer, vector<Reindeer>, decltype([](const Reindeer &a, const Reindeer &b) {
        return get<0>(a) > get<0>(b);
    })> queue;
    queue.push({0, start, RIGHT, {}});
    Grid<array<int, 4>> visited(maze.width, maze.height, {INT_MAX, INT_MAX, INT_MAX, INT_MAX});
    set<Coordinate> onBestPath = {};

    while (!queue.empty()) {
        auto [score, position, direction, route] = queue.top();
        queue.pop();

        if (position == finish) {
            onBestPath = route;
            onBestPath.insert(position);

            while (get<0>(queue.top()) == score) {
                if (get<1>(queue.top()) == position) {
                    auto otherRoute = get<3>(queue.top());
                    onBestPath.insert(otherRoute.begin(), otherRoute.end());
                }

                queue.pop();
            }

            return {score, onBestPath.size()};
        }
        
        if (visited[position][direction] < score) continue;
        visited[position][direction] = score;
        route.insert(position);
        
        if (maze[position(direction)] != '#') {
            queue.push({score+1, position(direction), direction, route});
        }
        if (maze[position(turnClockwise(direction))] != '#') {
            queue.push({score+1001, position(turnClockwise(direction)), turnClockwise(direction), route});
        }
        if (maze[position(turnAntiClockwise(direction))] != '#') {
            queue.push({score+1001, position(turnAntiClockwise(direction)), turnAntiClockwise(direction), route});
        }
    }

    return {0, 0};
}

int main() {
    CharGrid maze = {cin};
    auto [lowestScore, placesToSit] = findFastestRoute(maze, maze.findFirst('S'), maze.findFirst('E'));
    cout << "Lowest score: " << lowestScore << endl;
    cout << "Places to sit: " << placesToSit << endl;
    return 0;
}
