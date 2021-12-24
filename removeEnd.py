"""
Given a list, remove the n-th node from the end of the list
And return the head.

Example: 
list → [1, 2, 3, 4, 5], n → 2
output → [1, 2, 3, 5]
"""
def removeEnd(inputList = [1, 2, 3, 4, 5], n = 2):
    correctIndex = len(inputList) - n

    for char in inputList:
        if inputList.index(char) == correctIndex:
            inputList.remove(char)

    print ("The list is %s." %inputList)
    return inputList

def testing():
    if __name__ == "__main__":
        print ("Testing function...")

        try:
            assert removeEnd() == [1, 2, 3, 5]
        except:
            print ("Test 1 has failed.")
        try:
            assert removeEnd([12, 43, 54, 9], 4) == [43, 54, 9]
        except:
            print ("Test 2 has failed.")

#calling
testing()