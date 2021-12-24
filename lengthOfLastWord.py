"""
Given a string that consists of uppercase, lowercase,
and empty space characters, return the length of the last word in the string.
If the last word doesn’t exist, return 0.
Note: A word is defined as a character sequence
consisting of non-space characters.

Example:
input → Hello World
output → 5
"""
def lengthOfLastWord(string = "Hello World"):
    lst = string.split()

    try:
        last = lst[-1]
    except IndexError:
        return 0

    return len(last)

def testing():
    fails = 0

    try:
        assert lengthOfLastWord() == 5
    except AssertionError:
        print ("Test 1 has failed.")
        fails += 1
    try:
        assert lengthOfLastWord("a b c d") == 1
    except AssertionError:
        print ("Test 2 has failed.")
        fails += 1
    try:
        assert lengthOfLastWord("This is a test string.") == 7
    except AssertionError:
        print ("Test 3 has failed.")
        fails += 1
    try:
        assert lengthOfLastWord("1234") == 4
    except AssertionError:
        print ("Test 4 has failed.")
        fails += 1
    try:
        assert lengthOfLastWord("") == 0
    except AssertionError:
        print ("Test 5 has failed.")
        fails += 1
    try:
        assert lengthOfLastWord("    ") == 0
    except AssertionError:
        print ("Test 6 has failed.")
        fails += 1

    print ("The number of tests that failed are %a out of 6." %fails)

#calling
testing()
print ("Done!")