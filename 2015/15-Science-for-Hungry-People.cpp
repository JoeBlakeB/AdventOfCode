#include <array>
#include <iostream>
#include <sstream>
#include <vector>

#include "utils.cpp"

using namespace std;

constexpr unsigned int INGREDIENTS_SUM = 100;
constexpr unsigned int INGREDIENT_COUNT = 4;
constexpr unsigned int PROPERTY_COUNT = 5;

template <int ARRAY_SIZE>
class CountGenerator {
public:
    CountGenerator(unsigned int sum) : sum(sum) {
        numbers[0] = sum;
    }

    inline bool hasNext() { return hasNext_; }

    void next() {
        int nextRightIndex = getNextRightIndex();
        if (!hasNext_) return;
        numbers[nextRightIndex]--;
        numbers[nextRightIndex + 1] = sumRemaining(nextRightIndex);
        clearRight(nextRightIndex + 1);
    }

    inline unsigned int get(unsigned int index) {
        return numbers[index];
    }

private:
    const unsigned int sum;
    unsigned int numbers[ARRAY_SIZE] {0};
    bool hasNext_ = true;

    int getNextRightIndex() {
        for (int i = ARRAY_SIZE - 2; i >= 0; i--) {
            if (numbers[i] > 0) return i; 
        }
        hasNext_ = false;
        return -1;
    }

    unsigned int sumRemaining(int index) {
        int sumRemaining = 0;
        for (int i = 0; i <= index; i++) sumRemaining += numbers[i];
        return sum - sumRemaining;
    }

    void clearRight(int indexOfMiddle) {
        for (int i = indexOfMiddle + 1; i < ARRAY_SIZE; i++) numbers[i] = 0;
    }
};

array<int, INGREDIENT_COUNT * PROPERTY_COUNT> getIngredients(vector<string> input) {
    array<int, INGREDIENT_COUNT * PROPERTY_COUNT> ingredients;
    for (unsigned int i = 0; i < INGREDIENT_COUNT; i++) {
        string word;
        istringstream iss(input[i]);
        iss >> word;
        for (unsigned int p = 0; p < PROPERTY_COUNT; p++) {
            iss >> word >> word;
            ingredients[(i * PROPERTY_COUNT) + p] = stoi(word);
        }
    }
    return ingredients;
}

int main() {
    auto ingredients = getIngredients(getInputLinesVector());

    unsigned int bestCookieScore = 0;

    unsigned int bestCookieScore500Calorie = 0;

    for (auto ingredientCounts = CountGenerator<INGREDIENT_COUNT>(INGREDIENTS_SUM); ingredientCounts.hasNext(); ingredientCounts.next()) {
        int cookieProperties[PROPERTY_COUNT] = {0};

        for (unsigned int i = 0; i < INGREDIENT_COUNT; i++) {
            for (unsigned int p = 0; p < PROPERTY_COUNT-1; p++) {
                cookieProperties[p] += ingredientCounts.get(i) * ingredients[(i * PROPERTY_COUNT) + p];
            }
            cookieProperties[PROPERTY_COUNT-1] += ingredientCounts.get(i) * ingredients[(i * PROPERTY_COUNT) + PROPERTY_COUNT-1];
        }

        unsigned int score = 1;

        for (unsigned int p = 0; p < PROPERTY_COUNT-1; p++) {
            if (cookieProperties[p] < 0) score = 0;
            score *= cookieProperties[p];
        }

        if (score > bestCookieScore) {
            bestCookieScore = score;
        }

        if (score > bestCookieScore500Calorie && cookieProperties[PROPERTY_COUNT-1] == 500) {
            bestCookieScore500Calorie = score;
        }
    }

    cout << "Best Cookie Score: " << bestCookieScore << endl;
    cout << "Best 500 Calorie Cookie Score: " << bestCookieScore500Calorie << endl;

    return 0;
}