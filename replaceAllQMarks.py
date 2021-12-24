"""
Given a string containing only lowercase letters and the character "?",
Replace all the question marks with a letter,
But leave no consecutive letters.

Example 1:
input → "esx?d"
output → "esxad" or "esxbd" etc.
"""
def replaceAllQMarks(string="esx?d"):
    replace = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lst = stringToList(string)

    for char in range (len(lst)):
        if lst[char] == "?":
            try:
                while lst[char-1] == alphabet[replace] or lst[char+1] == alphabet[replace]:
                    replace += 1
            except IndexError:
                while lst[char-1] == alphabet[replace]:
                    replace += 1
            lst.pop(char)
            lst.insert(char, alphabet[replace])
            replace = 0

    returnValue = listToString(lst)
    print (returnValue)
    return returnValue

def listToString(inputList):
    resultString = ""

    for element in inputList:
        resultString += element

    return resultString

def stringToList(inputString):
    resultList = []

    for char in inputString:
        resultList.append(char)

    return resultList

#calling
replaceAllQMarks("eb?ad?")