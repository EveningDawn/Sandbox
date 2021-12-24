"""
Find if a number is perfect, meaning that all of its factors
add up (excluding itself) to itself.

Example 1:
input → 6
output → True

Example 2:
input → 8
output → False
"""
from math import fsum
def findPerfectNumber(num = 6):
    factorList = findFactors(num)

    if fsum(factorList) == num:
        return True
    else:
        return False

def findFactors(num):
    factorList = []

    for i in range (1, num):
        if num % i == 0:
            factorList.append(i)

    return factorList

def testing():
    print ("Testing...")

    try:
        assert findPerfectNumber() == True
    except AssertionError:
        print ("Test 1 failed.")
    try:
        assert findPerfectNumber(28) == True
    except AssertionError:
        print ("Test 2 failed.")
    try:
        assert findPerfectNumber(42) == False
    except AssertionError:
        print ("Test 3 failed.")
    try:
        assert findPerfectNumber(33550336) == True
    except AssertionError:
        print ("Test 4 failed.")
    try:
        assert findPerfectNumber(33550330) == False
    except AssertionError:
        print ("Test 5 failed.")

#calling
testing()
print ("Done!")