"""
Check an integer to see if it is a palindrome number.
Output True or False.
Rembeber, a palindrome number is a number that is the same both ways.

Example 1:
input → 121
output → True

Example 2:
input → -121
output → False

Example 3:
input → 120
output → False

Extra Work: See if you can do it without turning the input into a string.
"""
def findPalindromeNumber(num):
    numDigits = []

    #getting the digits of num
    appendToList = num % 10
    numDigits.append(appendToList)

def findPalindromeNumber_v2(num = 121):
    strNum = str(num)

    for digit in range(len(strNum)):
        if len(strNum) % 2 == 0:
            if strNum[digit] == strNum[-digit + 1]:
                continue
            else:
                #print (False)
                return False
        else:
            middleDigit = findMiddleDigit(num)
            if strNum[digit] != middleDigit:
                if strNum[digit] == strNum[-digit - 1]:
                    continue
                else:
                    #print (False)
                    return False

    #print (True)
    return True

def findMiddleDigit(num):
    strNum = str(num)

    if len(strNum) % 2 == 0:
        return None

    for digit in strNum:
        if strNum.index(digit) == len(strNum) // 2:
            #print ("The middle digit is %s." %digit)
            return digit

def testing():
    if __name__ == "__main__":
        print ("Testing function...")

        try:
            assert findPalindromeNumber_v2() == True
        except:
            print ("Test 1 has failed.")
        try:
            assert findPalindromeNumber_v2(-121) == False
        except:
            print ("Test 2 has failed.")
        try:
            assert findPalindromeNumber_v2(120) == False
        except:
            print ("Test 3 has failed.")
        try:
            assert findPalindromeNumber_v2(872393278) == True
        except:
            print ("Test 4 has failed.")

#calling
testing()
print ("Done!")