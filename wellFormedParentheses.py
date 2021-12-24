"""
Given a string containing just the characters "(" and ")",
Find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "())"
Ouput: 2

Example 2:
Input: "(()()("
Output: 4
"""
def wellFormedParentheses(inputP = ")()()()(("):
    numOfValidP = 0

    try:
        indexRight = inputP.find("(")
    except:
        #print ("No '(' character in inputP.")
        return 0

    try:
        if inputP[indexRight + 1] == ")":
            numOfValidP += 2
        else:
            inputP = removeChar(inputP, "(")
            try:
                indexRight = inputP.find("(")
            except:
                #print ("No '(' character in inputP.")
                return 0
            try:
                if inputP[indexRight + 1] == ")":
                    numOfValidP += 2
                else:
                    inputP = removeChar(inputP, "(")
            except IndexError:
                #print ("The number of valid parenthases in a row is %a. #1" %numOfValidP)
                return numOfValidP
    except IndexError:
        #print ("The number of valid parenthases in a row is %a. #1" %numOfValidP)
        return numOfValidP

    for char in range (indexRight + 2, len(inputP), 2):
        try:
            if inputP[char] == "(" and inputP[char + 1] == ")":
                numOfValidP += 2
            else:
                #print ("The number of valid parenthases in a row is %a. #2" %numOfValidP)
                return numOfValidP
        except IndexError:
            #print ("The number of valid parenthases in a row is %a. #3" %numOfValidP)
            return numOfValidP

    #print ("The number of valid parenthases in a row is %a. #4" %numOfValidP)
    return numOfValidP

def removeChar(string, rmv):
    indexRmv = string.find(rmv)
    stringList = []
    resultString = ""

    for char in string:
        stringList.append(char)

    stringList.pop(indexRmv)
    resultString = listToString(stringList)

    #print ("The original string is %s." %string)
    #print ("The string after the character %s was removed is %s." %(rmv, resultString))

    return resultString

def listToString(inputList):
    resultString = ""

    for element in inputList:
        resultString += element

    return resultString

def testing():
    if __name__ == "__main__":
        print ("Testing function...")
        wellFormedParentheses()

        try:
            assert wellFormedParentheses() == 6
        except AssertionError:
            print ("Test 1 failed.")
        try:
            assert wellFormedParentheses("())") == 2
        except AssertionError:
            print ("Test 2 failed.")
        try:
            assert wellFormedParentheses("(()()(") == 4
        except AssertionError:
            print ("Test 3 failed.")
        try:
            assert wellFormedParentheses(")))((") == 0
        except AssertionError:
            print ("Test 4 failed.")
        try:
            assert wellFormedParentheses("((((()()") == 4
        except AssertionError:
            print ("Test 5 failed.")

        print ("Testing done, code complete.")

#calling
testing()