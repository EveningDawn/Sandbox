#up top
weightsAndValues = {
    1: {"Weight": 5.0, "Value": 1000},
    2: {"Weight": 70.0, "Value": 1100},
    3: {"Weight": 30.0, "Value": 3000}
}

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

    """#fractional
    spaceLeft = sackCapacity - totalWeight
    if spaceLeft == 0 and spaceLeft < weight:
        return numberOfTheItem, theItemName, totalValue, "early"
    plusMore = weightsAndValues[theItemName]["Value"] / spaceLeft
    totalValue += plusMore
    numberOfTheItem += spaceLeft / weightsAndValues[theItemName]["Weight"]
    print (plusMore, spaceLeft)"""

    return chosenItems

#run
res = useGreedyAlgorithm(70, weightsAndValues)
print (res)