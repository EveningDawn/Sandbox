"""
Given an integer, reverse the digits.
For example, 324 will become 423.
-324 will become -423. And 120 will become 21.
"""
def reverseDigits(num):
    strNum = str(num)
    reverseStrNum = "" #for now

    if num < 0:
        strNum = removeChar(strNum, "-")
        for digit in range (len(strNum), 0, -1):
            reverseStrNum += strNum[digit - 1]
            reverseNum = int(reverseStrNum) * -1
    else:
        for digit in range (len(strNum), 0, -1):
            reverseStrNum += strNum[digit - 1]
            reverseNum = int(reverseStrNum)

    print ("%a reversed is %s." %(num, reverseNum))
    return reverseNum

def removeChar(string, rmv):
    indexRmv = string.find(rmv)
    resultString = ""

    for char in string:
        if string.find(char) != indexRmv:
            resultString += char

    #print ("The original string is %s." %string)
    #print ("The string after the character %s was removed is %s." %(rmv, resultString))

    return resultString

#call the func
reverseDigits(120)