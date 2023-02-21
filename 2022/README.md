# Advent of Code 2022

![](https://img.shields.io/badge/Stars%20-50_⭐-blue)
![](https://img.shields.io/badge/Lines_of_Code-1233-blue)

My solutions for the [Advent of Code 2022](https://adventofcode.com/2022) challenges.

Inputs for each task is in the `inputs` folder with as xx.txt where xx is the day number.

# Solution Explanations

## Day 1: Calorie Counting [🎄](https://adventofcode.com/2022/day/1) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/01-Calorie-Counting.py)

This one was just going through groups of numbers and calculating the sum of each group. The part 1 answer was just the highest of the sums. Part 2 was the sum of the highest three sums, so I sorted the list and added the last three to get the answer.

## Day 2: Rock Paper Scissors [🎄](https://adventofcode.com/2022/day/2) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/02-Rock-Paper-Scissors.py)

### Part 1

In this challenge you are given a list of predictions for a Rock Paper Scissors tournament and you needed to calculate the sum of scores for each round. I did this by creating a dictionary for the points you would get for each choice, and dictionaries for what you would need to do to win or draw against the opponent, giving more points for which outcome happens.

### Part 2

You find out that the predictions actually tells you what the result needs to be for each round and not what you need to choose. I made another dictionary for choosing which of the win, draw, or lose dictionaries is needed, and used that to calculate what needs to be chosen and the score for each round.

## Day 3: Rucksack Reorganization [🎄](https://adventofcode.com/2022/day/3) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/03-Rucksack-Reorganization.py)

### Part 1

You get a list of the contents of elves rucksacks and need to find what item is in both compartments for each elf, and use that to get the priority of the item. I did this by splitting each rucksack string into two strings, and looping through the first compartment until I got to the character that was also in the second compartment. I then used that to get the index of that character in the priority string and added that to the total for the final answer.

### Part 2

There are groups of three elves that all have one item which all of them have, you need to find the priority of this for each group like part 1 for the answer. I did this by looping through every third elf and checking each item in that elves backpack against elf+1 and elf+2.

## Day 4: Camp Cleanup [🎄](https://adventofcode.com/2022/day/4) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/04-Camp-Cleanup.py)

### Part 1

In this challenge you are given pairs of number ranges and have to count how many of these pairs where one range is completely inside the other range. To do this I just created a set from each range, and counted how many were a subset of the other.

### Part 2

You only needed to find out how many of the ranges overlapped, so I did it the same as part one but with the intersection function instead of the issubset function.

## Day 5: Supply Stacks [🎄](https://adventofcode.com/2022/day/5) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/05-Supply-Stacks.py)

### Part 1

You are given stacks of crates and instructions on how to move them. First I created a list for each stack by looping through each row of the input. Then I went through the instructions and moved the crates from one stack to another with pop and append if the from stack wasn't empty. To get the answer you need all of the top crates from each stack as a string.

### Part 2

The elves are using a different crane, CrateMover 9001 instead of 9000, which can move all of the crates in one move, meaning they keep their order. I did this by moving all crates to move into a picked up array, and then adding them to the new stack.

![Animation of Different Cranes](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-05.gif)

## Day 6: Tuning Trouble [🎄](https://adventofcode.com/2022/day/6) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/06-Tuning-Trouble.py)

### Part 1

For this one you needed to just find where in a string the first set of characters is where each character is different. I did this by going through each position, and checking if the next four characters from that were all different for part one. For part two I moved the previous solution into a function and just called it with the markerLength as 14 instead of 4 for the answer.

## Day 7: No Space Left On Device [🎄](https://adventofcode.com/2022/day/7) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/07-No-Space-Left-On-Device.py)

### Part 1

In this challenge you are given the terminal output of going through a filesysem and listing all directories and files. You then need to calculate the file structure and the sizes of directories as you ae only given the sizes of files. I did this by creating a list of all files/directories with each being a dictionary containing the name, size, type, and children so that I could access them with a path of names as well as easily loop through all of them. To get the answer I went through all files after calculating the structure and sizes, and summed the sizes of all directories over 100000.

### Part 2

As the challenge is about there not being enough space on the device to run a system update, you needed to find which directory was the smallest but which deleting would free up enough space. I did this by going through all directories and checking if the size was higher than the space needed, then finding the smallest of those for the answer.

## Day 8: Treetop Tree House [🎄](https://adventofcode.com/2022/day/8) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/08-Treetop-Tree-House.py)

### Part 1

You are given a grid of numbers representing the height of trees, with higher digits being taller trees. You needed to count how many trees are visible from outside the forest which I did by going around each of the edges of the grid and looking in, and counting how many times the number goes up past the previous maximum of that position. To make sure I didn't count trees twice from different edges, I stored all counted trees in an array and only counted the ones that weren't already in there.

### Part 2

For this part you needed to find the best tree to build a tree house by seeing where has the best views. This is done by getting the view distance from each direction and multiplying them together for a score. I did this by going through every position and finding the highest score which is the answer.

## Day 9: Rope Bridge [🎄](https://adventofcode.com/2022/day/9) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/09-Rope-Bridge.py)

### Part 1

For this one you had to simulate how the tail of a rope moves in a 2d grid when you move the head based on the input. You had to move the head in a direction a number of times and each time the head moved you would move the tail. I simply did this by if the tail was too far away, then moving it one closer, for each direction, which worked when it needed to move diagonally as well.

### Part 2

You now have to simulate a much longer rope, so instead of just two points, the head and tail, you now also had to simulate eight knots in between, which all worked the same was as part 1. I did this by making a list of all of the points, and after moving the head, moving each next knot/tail point if it needed to move.

## Day 10: Cathode Ray Tube [🎄](https://adventofcode.com/2022/day/10) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/10-Cathode-Ray-Tube.py)

### Part 1

For this one you are given a list of cpu instructions, noop which does nothing for one cycle, and addx which adds the value to the register after two cycles. You needed to find the value of the register at certain intervals. To do this I added an extra wait instruction before all addx instructions. Then all I needed to do was go through the instructions with each one being only one cycle, and if it was addx then I added the value to the register, and ignored the noop and wait instructions. At the intervals for the answer I added the value of the register to the answer.

### Part 2

The cpu is used for rendering an image on a 40x6 CRT screen, where you would draw a pixel if the register is within one of the cycleCounter. I did this by having an array of arrays of chars, and if a pixel should be drawn then I set the char to a solid block character in the same loop as part 1. To get the answer I just printed the CRT output which for me was:

```
▓▓▓▓░░▓▓░░▓░░░░░▓▓░░▓░░▓░▓░░░░▓▓▓░░░▓▓░░
▓░░░░▓░░▓░▓░░░░▓░░▓░▓░░▓░▓░░░░▓░░▓░▓░░▓░
▓▓▓░░▓░░▓░▓░░░░▓░░░░▓░░▓░▓░░░░▓░░▓░▓░░░░
▓░░░░▓▓▓▓░▓░░░░▓░▓▓░▓░░▓░▓░░░░▓▓▓░░▓░▓▓░
▓░░░░▓░░▓░▓░░░░▓░░▓░▓░░▓░▓░░░░▓░░░░▓░░▓░
▓▓▓▓░▓░░▓░▓▓▓▓░░▓▓▓░░▓▓░░▓▓▓▓░▓░░░░░▓▓▓░
```

## Day 11: Monkey in the Middle [🎄](https://adventofcode.com/2022/day/11) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/11-Monkey-in-the-Middle.py)

### Part 1

You are given a list of monkeys, what items they start with, and what they do to decide which monkey to throw each item to when it is their turn. I did this by creating an object for each monkey and storing them in a list. Then for each round I would make each monkey throw all items they have. After 20 rounds, you multiply the two monkeys with the most items together to get the answer.

### Part 2

This part was the same as part one, but instead of only 20 rounds you needed to 10 thousand, and that the worry, which used by monkeys for deciding which monkey to throw to, would quickly increase and take a very long to run. I solved this by just moduloing the worry by the product of all monkeys calculation number so that they would all give the same answer before and after moduloing, and the number would not take too long to calculate. The code was able to simulate 10 thousand rounds in half a second.

## Day 12: Hill Climbing Algorithm [🎄](https://adventofcode.com/2022/day/12) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/12-Hill-Climbing-Algorithm.py)

For this challenge you needed to find the shortest path to the top of the hill where you could only go up one elevation at a time. To do this I needed to learn a path finding algorithm, and I decided to learn how A* works and use that. The elevations were represented as the alphabet with a being the lowest and z being the highest, however the start and end were represented as S and E which caused me some confusion as I didn't know they were the same elevations as a and z. After I realized that I was able to get the right answer and the path taken was:

![Map of Hill Climbing Algorithm](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-12.png)

For part two, all you needed to find which of the furthest left points had the shortest path to the top, so I just ran the simulation multiple times.

## Day 13: Distress Signal [🎄](https://adventofcode.com/2022/day/13) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/13-Distress-Signal.py)

### Part 1

In this challenge, you are given pairs of packets which are lists with more lists or numbers, and you have to see which ones are in the right order based on a few rules. I did this by creating a class for these packets with a less than magic method for easily comparing them. This called a compare method, which would run recursively for nested lists. Then I got the answer by going through the pairs and adding the index of the pair to the answer if it was in the right order.

### Part 2

The reason I did part one with a magic method was so that I could easily use the built in sort method on the packets list. This part requires you to find a decoder key which you get by adding two divider packets, and multiplying their index after sorting to get the answer.

## Day 14: Regolith Reservoir [🎄](https://adventofcode.com/2022/day/14) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/14-Regolith-Reservoir.py)

### Part 1

This challenge requires you to simulate sand falling in a cave and you are only given scans of rocks in the cave. First I needed to turn these scans into an actual cave structure as a 2d array. After this I needed to simulate the sand falling, which started at the top, and could go directly below, or below left or right. If it cannot fall any further, I added it to the grid, then simulated the next sand, and repeated this until some sand fell into the void. The answer was the number of sand until that happened.

![Animation of Regolith Reservoir Part 1](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-14-1.gif)

### Part 2

It turns out there is no void under the scanned cave, but a floor one below the lowest point, and I made it so if a sand reached one below it would automatically stop falling. The answer is the amount of sand until you cannot add any more sand. As there was no way to know how wide the cave would be with all of the sand creating a pyramid, I made a Grid object for managing the grid, which would allow me to add sand off the edge of the grid and it would automatically expand the grid without coordinates changing.

![Animation of Regolith Reservoir Part 2](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-14-2.gif)

## Day 15: Beacon Exclusion Zone [🎄](https://adventofcode.com/2022/day/15) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/15-Beacon-Exclusion-Zone.py)

### Part 1

You are given a list of sensors, their position, and the position of the closest beacon. This means that for each sensor, there is a radius where there cannot possibly be any beacons, and I did this by adding the exclusion zones to a list as ranges, which I then converted to just one list of all numbers to remove duplicates and the scanned beacons. The answer was the final length of the list.

### Part 2

In a 4 million by 4 million grid, there is just one location which the sensors did not detect. It is not realistic to go through all possible locations as there would be 16 trillion locations to go through. Instead I went through all y values, and for x I started at 0 and would go to the end of the first exclusion zone which that location is in. This is not very efficient as it still needs to go through 4 million rows of this, and it takes a while to run, but it will find the answer, which is the location with no detected beacon, in less than a minute.

## Day 16: Proboscidea Volcanium [🎄](https://adventofcode.com/2022/day/16) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/16-Proboscidea-Volcanium.py)

### Part 1

You are given a list of valves with flow rates, and tunnels leading to other valves, and you need to find out which order you open the valves in for the most pressure to be released in 30 minutes. Travelling between valves once takes one minute, and so does opening a valve. So there are too many to open them all and there is no way to know if opening the highest rate valve first is better, or if opening the closest rate valve first is better, so the only way I could think to do this was to try everything. I used a recursive function for simulating opening valves, which would try all possible valve combinations by calling itself with one of them chosen for each stage. I optimized this by calculating the time to travel to each of them first, and skipping that amount of time so the function would only call itself every time it forks. The highest possible amount released would be returned, and it would eventually go back to the original call, which would return the answer, and this only takes half a second to run.

### Part 2

You spend the first four minutes training an elephant on how to open valves, so have 26 minutes to simulate two people opening valves. I struggled with this one a lot as I originally tried to change my original function to allow for multiple people opening valves, but this was not efficient enough to run in a reasonable amount of time. I ended up just splitting the list of valves to travel to in pairs, with every possible combination of pairs. Then running the original function twice on each pair and adding the output together, the highest of the pairs would then be the answer and this took about a minute to run.

## Day 17: Pyroclastic Flow [🎄](https://adventofcode.com/2022/day/17) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/17-Pyroclastic-Flow.py)

### Part 1

This challenge is similar to tetris, you are given five shapes and a series of movements that happen while those shapes are falling. You need to simulate this and see how high the tower is after 2022 rocks have fallen. I did this with a grid object with methods for the four parts of this. One for dropping a rock would use the rest of the methods to decide where the new rock will go. One for moving the rock left or right depending on the input. Another for checking if the rock is colliding and should stop falling. And one for adding a rock in the right place after it has.

![Animation of Pyroclastic Flow Part 1](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-17-1.gif)

### Part 2

You now need to get the tower height after a trillion rocks have fell. This is obviously not going to be possible so you needed to find a pattern and luckily this happens as when the movement input finishes it loops from the beginning again and the tower shape is the same. I continued simulating until the movement sequence reset, and saved the height, then did it again so that I would know the change in height each sequence. Then I skipped the amount of sequences until it was almost at a trillion, then finished simulating properly to exactly a trillion rocks. This way I could get the answer in half a second.

![Animation of Pyroclastic Flow Part 2](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-17-2.gif)

## Day 18: Boiling Boulders [🎄](https://adventofcode.com/2022/day/18) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/18-Boiling-Boulders.py)

### Part 1

For this challenge you are given a 3d ball of lava scanned as coordinates of cubes, and you needed to find the surface area. I did this by creating a 3d array for the shape and adding the input coordinates to it. I then went through all coordinates in the scan where there was a cube, and for each side of the cubes, if there was no cube I would add one to the surface area. I used lambdas for getting the new coordinates for each side.

### Part 2

There are a lot of air bubbles inside the lava ball and only should count the external surface area. I got the answer by before adding one to the surface area, I used a function to check if its external, which would check if you could get out of the grid from that position. This used breadth first search to check all possible directions for the few overhangs in the shape, and added a cache to the function so it would only use BFS the first few times the program runs.

## Day 19: Not Enough Minerals [🎄](https://adventofcode.com/2022/day/19) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/19-Not-Enough-Minerals.py)

### Part 1

This one is similar to day 16, you don't know what order you should do things and I did every possible combination. This time you are given a list of blueprints for making various robots to collect various materials, and your aim is to collect the most geodes in 24 minutes. Like day 16 I used another recursive function to try every possible combination which returned the highest possible amount of geodes collected. To speed it up I added a cache so the same simulation would not need to run multiple times, which sped up the process a lot. I also tried to do this challenge with an iterative breadth first search, but it was slower than the recursive function even with optimising and removing duplicates so I stuck with the recursive function. I really struggled with this one as some of the optimisations were not obvious at first. One of them being that if you already have enough until time runs out you don't need to make more of that type of robot.

### Part 2

You now need to run the simulation for 32 minutes, this being so much higher meant that the time to simulate each blueprint was exponentially higher. I tried to find optimisations for a while and only found a few, one being that you don't need to make a robot if it would mean your production for a material was higher than the quickest way you could use that material, but it didn't speed it up very much. I eventually decided to just run it and see how long it would take, which did give me the right answer, but took about 20 minutes to run.

## Day 20: Grove Positioning System [🎄](https://adventofcode.com/2022/day/20) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/20-Grove-Positioning-System.py)

### Part 1

You are given a series of numbers and you have to mix them by moving them in the array by that amount. To do this you needed to copy the array as this needs to be done to all items, in the original order. I did this by getting the index and removing the item from the array, adding it to the index, then adding it back to the array with the new index. The answer was then the 1000th, 2000th, 3000th value of the array multiplied together, which to get you needed to modulo by the length of the array for each index. A problem I faced with the real input was that there are multiple numbers that are the same. To make sure that I am moving the right one, I added a # and index to the end of the number so that I would always move the right one. This meant I needed to remove the # and convert between string and int. While writing this I realized that's not the best way to do it, I should have used a tuple with the index as the second value to make each tuple unique. However, it only takes a few seconds to run as there aren't many duplicates so I haven't changed it.

### Part 2

You now needed to do this mixing ten times, but also needed to multiply all numbers by a key. This meant that the new index would be out of the range of the array, so you needed to use modulo with the length of the array to get the new index. I was then able to get the correct answer

## Day 21: Monkey Maths [🎄](https://adventofcode.com/2022/day/21) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/21-Monkey-Maths.py)

### Part 1

You are given a list of monkeys, and they all have either a number, or a calculation for their number. You need to calculate the value of the monkey called root, which means finding the value of the two monkeys in its calculation, which means you need their calculation, and so on. I did this with a recursive function, if the monkey was just a number it would return that, and if it were a calculation it would solve it before returning the value. 

### Part 2

The humn monkey is actually you, and the root monkey is actually comparing their two values, so you need to work out the number you need to have for the values to be the same. I did this by creating the formula for it by making each calculation go in reverse to get the value the other half of the monkeys calculated. I then just used eval to solve the formula at the end for the answer.

## Day 22: Monkey Map [🎄](https://adventofcode.com/2022/day/22) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/22-Monkey-Map.py)

### Part 1

You are given a map with places you can and cant go, and you wrap to the opposite side if you go off the edge. To get the answer you need to simulate travelling across the map and see where you end, and then doing a formula on the coordinates. I did this by creating a board object with the map in it, and just travelling across it. There was also a function to automatically wrap to the other side if you went off. After you finish the directions that you are given, I did the formula on the coordinates to get the answer.

### Part 2

It turns out that the funny shaped board isn't actually a board, but a cube. This meant that instead of wrapping to the other side, you wrap to the next face fo the cube which was complicated. I created a cube class which inherited from the board class so I only needed to recreate the wrap function. I did this by manually adding each of the wraps to a dictionary, and seeing which one it should be by seeing if the coordinates were in the range. This is not the best way to do it as if there was a different shaped board, this would not work, but the creator of advent of code said on reddit that everyone's input would have the same cube net.

![Wraps of Monkey Map Part 2](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-22-2.png)

## Day 23: Unstable Diffusion [🎄](https://adventofcode.com/2022/day/23) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/23-Unstable-Diffusion.py)


You are given a grid of where elves are, and need to move each of them according to a set of rules to move them similar to Conway's Game of Life. I did this by having two classes, the crater where all of the elves will be, and the elf class for each of the elves. For each round I created a grid from their positions, which the elves used to plan to move, then the elves would check that they are able to move, then they would finally move. For part one you only needed to do the first ten rounds of this and count the number of ground tiles between them. And then for part two you needed to simulate until none of them needed to move, and count how many rounds it took for the answer.

![Animation of Unstable Diffusion](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-23.gif)

## Day 24: Blizzard Basin [🎄](https://adventofcode.com/2022/day/24) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/24-Blizzard-Basin.py)

In this challenge you are given a grid of directions that blizzards are moving in and you needed to simulate these blizzards moving each minute. You could also move once each minute to any place where a blizzard would not be. For this I used breadth first search to find all places where you could be each round, and as soon as you get to the end of the grid, you have found the shortest path. For part one you needed to get from the top left position to the bottom right position. For part two, all you needed to do was to go back to the start, then back to the end again. As I did the valley as an object, all I needed to do was to call the cross valley function two more times.

![Animation of Blizzard Basin](https://raw.githubusercontent.com/JoeBlakeB/AdventOfCode/main/.github/images/2022-24.gif)

## Day 25: Full of Hot Air [🎄](https://adventofcode.com/2022/day/25) [🔗](https://github.com/JoeBlakeB/AdventOfCode/blob/main/2022/25-Full-of-Hot-Air.py)

The final challenge was about a base-5 number system called SNAFU™, but unlike regular base-5, these numbers can only go up to 2, and to go higher you would need to add one to the next digit and represent the current digit as one or two minus signs. For example to convert the SNAFU™ number `2=2` to base-10, you would do the following:

| 25s | 5s | 1s |
|-|-|-|
| `2` | `=` | `2` |
| `2` | `-2` | `2` |
| `2`\*25 | `-2`\*5 | `2`\*1 |
| `50` | `-10` | `2` |

So the base-10 number would be `50 - 10 + 2` which is `42`. To complete the challenge you needed to sum these numbers, and to do so you would need to convert them to base-10 before summing them, and then convert the result back into SNAFU™ for the answer.