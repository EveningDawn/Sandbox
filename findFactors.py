#Find the factors of a number

from math import sqrt
def findFactors(num):
    squareRoot = int(sqrt(num))
    factorList = []

    for possibleFactor in range (1, squareRoot + 1):
        if num % possibleFactor == 0:
            factorList.append(possibleFactor)
            factorList.append(num // possibleFactor)

    factorList = removeDuplicates(factorList)
    factorList.sort()
    return factorList

def removeDuplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)

    return result

#calling
findFactors(10)