// Copyright (C) 2024 Joe Baker (JoeBlakeB)
// Advent of Code 2023 - Day 20: Pulse Propagation
// Usage:
//     scripts/cppRun.sh 2023/20-Pulse-Propagation.cpp < 2023/inputs/20.txt

#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;


struct PulseQueueItem {
    short sender;
    short receiver;
    bool highPulse;
};

typedef queue<PulseQueueItem> PulseQueue;


class Module {
protected:
    short id;
    vector<short> inputModules, outputModules;

    // Sends pulse to all output modules
    inline void output(bool highPulse, PulseQueue &pulseQueue) {
        for (size_t i = 0; i < outputModules.size(); i++) {
            pulseQueue.push({this->id, outputModules[i], highPulse});
        }
    }

public:
    Module(short id, vector<short> outputModules) : id(id), inputModules(), outputModules(outputModules) {}

    virtual ~Module() {}

    // Processes a pulse and saves any resulting output pulses to the pulse queue
    virtual void pulse(bool highPulse, short sender, PulseQueue& pulseQueue) {
        (void)highPulse; (void)sender; (void)pulseQueue;
    }

    // Gets the current state of the module, if any
    virtual char state() { return 0; }

    // Resets the modules state, if any
    virtual void reset() {}

    // Add an input module to this module
    virtual void addInput(short newInput) { inputModules.push_back(newInput); }

    // Get the list of input module IDs
    virtual vector<short> getInputList() { return inputModules; }
};


class FlipFlop : public Module {
private:
    bool power;
    
public:
    FlipFlop(short id, vector<short> outputModules) : Module(id, outputModules), power(false) { }

    // Flips between sending high and low pulses, only when low are received
    void pulse(bool highPulse, short, PulseQueue& pulseQueue) override {
        if (!highPulse) {
            power = !power;
            output(power, pulseQueue);
        }
    }

    // The current power state
    char state() override { return power; }

    // Resets the power to off
    void reset() override { power = false; }
};


class Conjunction : public Module {
private:
    vector<pair<short, bool>> inputModules;
    bool receivedHigh;

public:
  Conjunction(short id, vector<short> outputModules) : Module(id, outputModules), inputModules(), receivedHigh(false) {}

    // Remembers the pulses from its input modules, if all are high,
    // it will send a low to its recepients, otherwise it will send high
    void pulse(bool inputHighPulse, short sender, PulseQueue& pulseQueue) override {
        bool outputHighPulse = false;

        for (size_t i = 0; i < inputModules.size() && (sender || !outputHighPulse); i++) {
            if (sender && inputModules[i].first == sender) {
                inputModules[i].second = inputHighPulse;
                sender = 0;
            }

            if (!inputModules[i].second) {
                outputHighPulse = true;
                receivedHigh = true;
            }
        }
        
        output(outputHighPulse, pulseQueue);
    }

    // The last pulses for its input modules, the last bit for if a high pulse has been received yet
    char state() override {
        int value = 0;
        for (size_t i = 0; i < inputModules.size(); i++) {
            value = (value + inputModules[i].second) << 1;
        }
        return value + receivedHigh;
    }

    // Resets all input modues previous state to low
    void reset() override {
        receivedHigh = false;
        for (size_t i = 0; i < inputModules.size(); i++) {
            inputModules[i].second = false;
        }
    }

    // Add a module to its list with its previous pulse being set to low
    void addInput(short newInput) override { inputModules.push_back({newInput, false}); }

    // Get the list of input module IDs
    vector<short> getInputList() override {
        vector<short> inputList;
        for (size_t i = 0; i < inputModules.size(); i++) {
            inputList.push_back(inputModules[i].first);
        }
        return inputList;
    }
};


class Broadcaster : public Module {
public:
    Broadcaster(short id, vector<short> outputModules) : Module(id, outputModules) {}

    // Sends its pulse to all connected modules
    void pulse(bool highPulse, short, PulseQueue& pulseQueue) override {
        output(highPulse, pulseQueue);
    }

    // Broadcasters do not have a state, return 0
    char state() override { return 0; }
};


class Output : public Module {
private:
    char lastPulse;
    
public:
    Output(short id, vector<short> outputModules) : Module(id, outputModules), lastPulse(0) { }

    // Saves the last pulse, low being 1, high being 2
    void pulse(bool inputHighPulse, short, PulseQueue&) override {
        lastPulse = inputHighPulse + 1;
    }

    // The current power state
    char state() override { return lastPulse; }

    // Resets the power to off
    void reset() override { lastPulse = 0; }
};


constexpr short getID(string moduleName) {
    return moduleName[0] + (moduleName.size() >= 2 ? (moduleName[1] << 8) : 0);
}


class Network {
private:
    map<short, Module*> modules;

public:
    Network(istream &inputstream) {
        string line;
        vector<pair<short, vector<short>>> modulesAndOutputsTemp;

        // Create the modules
        while (getline(inputstream, line) && line != "") {
            vector<short> outputModules;
            size_t i = 0;

            // Save the first and second chars in a short for efficiency
            short thisModuleID = line[1];
            if (line[2] != ' ') {
                thisModuleID += line[2] << 8;
            }

            if (line[0] == 'b') {
                thisModuleID = 0;
            }

            if (modules.find(thisModuleID) != modules.end()) {
                exit(1);
            }

            // Go to the start of the output list
            do { i++; } while (line[i] != '>' || line[i+1] != ' '); i+= 2;

            // Get the output modules for this module
            while (i < line.size()) {
                short outputModule = line[i++];

                if (i < line.size() && line[i] != ',') {
                    outputModule += line[i++] << 8;
                }

                while (i < line.size()) {
                    if (line[i++] == ' ') {
                        break;
                    }
                }

                outputModules.push_back(outputModule);
            }

            modulesAndOutputsTemp.push_back({thisModuleID, outputModules});
            
            Module* thisModule = nullptr;
            if (line[0] == 'b') {
                thisModule = new Broadcaster(thisModuleID, outputModules);
            } else if (line[0] == '%') {
                thisModule = new FlipFlop(thisModuleID, outputModules);
            } else if (line[0] == '&') {
                thisModule = new Conjunction(thisModuleID, outputModules);
            } else {
                cout << "Error: Invalid line, unknown module type: " << line[0] << endl;
                exit(1);
            }

            modules.insert({thisModuleID, thisModule});
        }

        // Go through the modules and output lists again to add the inputs
        for (auto it = modulesAndOutputsTemp.begin(); it != modulesAndOutputsTemp.end(); it++) {
            const short& inputModule = it->first;
            const vector<short>& moduleList = it->second;

            for (size_t i = 0; i < moduleList.size(); i++) {
                // Module does not exist, create dummy input only module (output, tx)
                if (!exists(moduleList[i])) {
                    modules.insert({moduleList[i], new Output(moduleList[i], {})});
                }

                modules[moduleList[i]]->addInput(inputModule);
            }
        }
    }

    ~Network() {
        for (auto it = modules.begin(); it != modules.end(); it++) {
            delete it->second;
        }
    }

    Network(const Network& other) = delete;
    Network(Network&& other) = delete;
    Network& operator=(const Network& other) = delete;
    Network& operator=(Network&& other) = delete;

    // Press the button once and process its following pulses, returns a pair of the count of low and high pulses
    pair<long long int, long long int> pressButton() {
        PulseQueue pulseQueue({{0, 0, false}});
        int pulseCounts[2] = {0, 0};

        while (!pulseQueue.empty()) {
            PulseQueueItem nextPulse = pulseQueue.front();
            pulseQueue.pop();

            // cout << nextPulse.sender << " > " << nextPulse.highPulse << " > " << nextPulse.receiver << endl;

            pulseCounts[nextPulse.highPulse]++;
            modules[nextPulse.receiver]->pulse(nextPulse.highPulse, nextPulse.sender, pulseQueue);
        }

        return {pulseCounts[0], pulseCounts[1]};
    }
    
    // Press the button a certain amount of times
    pair<long long int, long long int> pressButton(int count) {
        pair<long long int, long long int> pulseCounts = {0, 0};

        for (int i = 0; i < count; i++) {
            auto nextCounts = pressButton();
            pulseCounts.first += nextCounts.first;
            pulseCounts.second += nextCounts.second;
        }
        
        return pulseCounts;
    }

    // Reset all modules in the network
    void reset() {
        for (auto it = modules.begin(); it != modules.end(); it++) {
            it->second->reset();
        }
    }

    char state(short moduleID) {
        return modules[moduleID]->state();
    }

    bool exists(short moduleID) {
        return modules.count(moduleID);
    }

    // Get the closest junction (module with more than one input) to the output (rx)
    vector<short> getInputsForFirstJunction(short currentModuleID) {
        int inputCount;
        vector<short> inputsList;
        do {
            inputsList = modules[currentModuleID]->getInputList();
            currentModuleID = inputsList.front();
            inputCount = inputsList.size();
        } while (inputCount == 1);
        return inputsList;
    }
};


int main() {
    Network network(cin);

    auto pulseCounts = network.pressButton(1000);
    cout << "Product of push types after 1000 pushes: " << pulseCounts.first * pulseCounts.second << endl;

    constexpr short outputID = getID("rx"); 
    if (network.exists(outputID)) {
        network.reset();
        
        // Get the list of inputs to the final conjunction
        vector<short> finalConjunctionInputs = network.getInputsForFirstJunction(outputID);

        long long int product = 1;
        int presses = 0;

        // Get the product of the amount of times it takes for each of the inputs
        // to the final conjunction to receive their first low pulse
        while (!finalConjunctionInputs.empty()) {
            network.pressButton();
            presses++;
            for (size_t i = 0; i < finalConjunctionInputs.size(); i++) {
                if (network.state(finalConjunctionInputs[i]) % 2) {
                    product *= presses;
                    finalConjunctionInputs.erase(finalConjunctionInputs.begin() + i);
                }
            }
        }
        
        cout << "Presses required for a low pulse to the \"rx\" module: " << product << endl;
    } else {
        cout << "Network does not contain the \"rx\" module" << endl;
    }
    
    return 0;
} 

