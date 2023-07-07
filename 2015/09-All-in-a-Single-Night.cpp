#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

#include "utils.cpp"

class Map {
  public:
    Map(std::vector<std::string> distancesInput) {
        for (std::string distanceBetweenLocations : distancesInput) {
            std::istringstream iss(distanceBetweenLocations);
            std::string location1, location2, distance;
            iss >> location1 >> location2 >> location2 >> distance >> distance;
            addLocation(location1);
            addLocation(location2);
            distances[locationPair(location1, location2)] = std::stoi(distance);
        }
    }

    std::pair<std::string, unsigned int> findRoute(bool shortest) {
        std::pair<std::string, unsigned int> shortestRoute = {"", shortest ? -1 : 0};

        for (std::string location : locations) {
            std::pair<std::string, unsigned int> route =
                findShortestRouteRecursive(location, visitLocation(locations, location), shortest);
            if ((shortest && route.second < shortestRoute.second) ||
                (!shortest && route.second > shortestRoute.second)) {
                shortestRoute = route;
            }
        }
        return shortestRoute;
    }

  private:
    std::vector<std::string> locations;
    std::map<std::string, unsigned int> distances;

    void addLocation(std::string location) {
        if (std::find(locations.begin(), locations.end(), location) == locations.end()) {
            locations.push_back(location);
        }
    }

    std::string locationPair(std::string location1, std::string location2) {
        if (location1 < location2) {
            return location1 + " " + location2;
        } else {
            return location2 + " " + location1;
        }
    }

    std::vector<std::string> visitLocation(
        const std::vector<std::string> &previouslyUnvisited,
        std::string location
    ) {
        std::vector<std::string> nowUnvisited;
        for (std::string i : previouslyUnvisited) {
            if (i != location) {
                nowUnvisited.push_back(i);
            }
        }
        return nowUnvisited;
    }

    std::pair<std::string, unsigned int> findShortestRouteRecursive(
        std::string currentLocation,
        std::vector<std::string> unvisitedLocations,
        bool shortest
    ) {
        if (unvisitedLocations.size() == 1) {
            return {
                currentLocation + " -> " + unvisitedLocations[0],
                distances[locationPair(currentLocation,
                                       unvisitedLocations[0])]
            };
        } else {
            std::pair<std::string, unsigned int> shortestNextRoute = {"", shortest ? -1 : 0};

            for (std::string location : unvisitedLocations) {
                std::pair<std::string, unsigned int> route =
                    findShortestRouteRecursive(location, visitLocation(unvisitedLocations, location), shortest);
                unsigned int distanceToNextLocation = distances[locationPair(currentLocation, location)];
                if ((shortest && route.second + distanceToNextLocation < shortestNextRoute.second) ||
                    (!shortest && route.second + distanceToNextLocation > shortestNextRoute.second)) {
                    shortestNextRoute = route;
                    shortestNextRoute.second += distanceToNextLocation;
                }
            }

            return {
                currentLocation + " -> " + shortestNextRoute.first,
                shortestNextRoute.second};
        }
    }
};

int main() {
    Map map(getInputLinesVector());
    std::pair<std::string, unsigned int> shortestRoute = map.findRoute(true);
    std::cout << shortestRoute.first << " = " << shortestRoute.second << std::endl;
    std::pair<std::string, unsigned int> longestRoute = map.findRoute(false);
    std::cout << longestRoute.first << " = " << longestRoute.second << std::endl;

    return 0;
}