#right at the top!
weightsAndValues = {
    1: {"Weight": 5.0, "Value": 1000},
    2: {"Weight": 70.0, "Value": 1100},
    3: {"Weight": 30.0, "Value": 3000}
}

def useGreedyAlgorithm(sackCapacity, weightsAndValues): #function with two parameters; weightsAndValues is dict, sackCapacity is int
    #print (weightsAndValues)
    totalWeight = 0 #preset
    numberOfTheItem = 0 #preset
    totalValue = 0 #preset

    lst = len(weightsAndValues) * [None]
    index = 0
    for item in weightsAndValues:
        weight, value = weightsAndValues[item]["Weight"], weightsAndValues[item]["Value"]
        #print (weight, value)
        unitValue = findUnitValue(weight, value)
        lst[index] = unitValue
        index += 1

    #find some key variables
    theItemValue = max(lst)
    #print ("I got here.", lst)
    for item in weightsAndValues:
        modifiedItem = item - 1
        weight, value = weightsAndValues[item]["Weight"], weightsAndValues[item]["Value"]
        toCheck = findUnitValue(weight, value)
        if toCheck == theItemValue:
            theItemName = item
            break
            #print ("I got here. (0.5)")
    #print (theItemValue, theItemName, lst)

    #print ("I got here. (2)")
    while totalWeight < sackCapacity:
        weight = weightsAndValues[theItemName]["Weight"]
        if sackCapacity < totalWeight + weight:
            break
        else:
            totalWeight += weight
            totalValue += weightsAndValues[item]["Value"]
            numberOfTheItem += 1
        #print ("I got here. (" + str(numberOfTheItem+2) + ")")

    #fractional
    spaceLeft = sackCapacity - totalWeight
    if spaceLeft == 0 and spaceLeft < weight:
        return numberOfTheItem, theItemName, totalValue, "early"
    plusMore = weightsAndValues[theItemName]["Value"] / spaceLeft
    totalValue += plusMore
    numberOfTheItem += spaceLeft / weightsAndValues[theItemName]["Weight"]
    print (plusMore, spaceLeft)

    return numberOfTheItem, theItemName, totalValue

def findUnitValue(weight, value):
    unitValue = value / weight

    #print (unitValue)
    return unitValue

#print(findUnitValue(3, 1100)) #test the function

#run
res = useGreedyAlgorithm(70, weightsAndValues)
part1 = "Item #" + str(res[1])
part2 = " fit into the sack " + str(res[0]) + " times."
part3 = " The total value of the things that the theif stole is $" + str(res[2]) + "!"
print (part1 + part2 + part3)