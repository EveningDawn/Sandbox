"""
Greedy algorithms aim to make the optimal choice at that given moment.
For each step, it chooses the optimal choice, without knowing the future.
It attempts to find the globally optimal way to solve the entire problem using this method.

(1) 0 - 1 knapsack problem:
The problem restricts the number of copies of each kind of item to zero or one, which means that items cannot be broken
and the person should take the item as a whole or they should leave it.

Given a set of items, each with a weight and a value along with a maximum weight capacity (sack capacity), maximize the VALUE of the sack.
For example, I have a sack with a weight capacity 70 pounds. I have three items with the same value per weight unit:
item 1: weight 30, value 30
item 2: weight 40, value 40
item 3: weight 50, value 50
The greedy algorithm will choose item 3 first, then it cannot choose 1 or 2, because the total will be more then 70.
Using the greedy algorithm for this example, you won't get the best choice.

But if the three items are:
item 1: weight 15, value 15
item 2: weight 40, value 40
item 3: weight 20, value 20
The greedy algorithm will choose item 2 first, then 3. The best is 60. It can get the best solution with greedy algorithm.

That being said, greedy algorithm cannot guarantee to get the best solution for 0-1 knapsack problem.

Now, the question is: given a list of items with weights, values, and a sack with a weight capacity,
use the greedy algorithm to find a solution to try to maximize the value of the items the sack holds.
"""

def useGreedyAlgorithm(sackCapacity, weightsAndValues): #function with two parameters; weightsAndValues is dict, sackCapacity is int
    totalWeight = 0 #preset
    chosenItems = [] #preset

    while totalWeight <= sackCapacity: #while loop
        maxValue = 0 #reset/preset
        maxValueNum = 0 #reset/preset
        for item in weightsAndValues: #go through every value to find the max
            #print (item)
            if weightsAndValues[item]["Value"] > maxValue and totalWeight + weightsAndValues[item]["Weight"] <= sackCapacity: #compare and check
                maxValue = weightsAndValues[item]["Value"] #change max to make better comparisons
                maxValueNum = item #reference for later
        if maxValueNum == 0:
            break
        totalWeight += weightsAndValues[maxValueNum]["Weight"]
        chosenItems.append("item"+str(maxValueNum))
        del weightsAndValues[maxValueNum]

    return chosenItems

#call
weightsAndValues = {
    1: {"Weight": 15, "Value": 15},
    2: {"Weight": 40, "Value": 40},
    3: {"Weight": 20, "Value": 20}
}
useGreedyAlgorithm(70, weightsAndValues)