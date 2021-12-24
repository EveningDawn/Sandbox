from .greedyAlgorithm import useGreedyAlgorithm

def findUnitValue(weight, value):
    unitValue = value / weight

    #print (unitValue)
    return unitValue

#print(findUnitValue(2, 10000)) #test the function

weightsAndValues = {
    1: {"Weight": 1, "Value": 1000},
    2: {"Weight": 70, "Value": 1100},
    3: {"Weight": 30, "Value": 3000}
}

def run(): #yawn, what a boring name
    for item in weightsAndValues:
        unitValue = findUnitValue(weightsAndValues[item]["Weight"], weightsAndValues[item]["Value"])
        weightsAndValues[item]["Value"] = unitValue

    res = useGreedyAlgorithm(70, weightsAndValues)
    print (res)