"""
Given a list and a value, remove all elements of that
value and return the new length of the list.

Example 1:
list → [3, 2, 3, 2]
value → 3
output → 2

Example 2:
list → [0, 1, 2, 2, 3, 0, 4, 2]
value → 2
output → 5
"""
def removeValue(lst, value):
    count = lst.count(value)
    i = 0

    while i < count:
        lst.remove(value)
        i += 1

    return len(lst)

def testing():
    try:
        removeValue([3, 2, 2, 3], 2) == 2
    except AssertionError:
        print ("Test 1 has failed.")
    try:
        removeValue([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    except AssertionError:
        print ("Test 2 has failed.")


#calling
testing()
print ("Done!")