"""
For example, given a sorted list A = [6, 8, 10],
and an unsorted list B = [5, 2, 6], insert the numbers one by one from list B into A,
so A will still be a sorted list. The result list is [2, 5, 6, 6, 8, 10]

Note: Please do not use the embedded python method for the insertion.
You can use len(list).
"""
from .insertNum import insertNum #run code in tests.py

debug = True

def insertList(A, B):
    #get list/s
    combined = [None] * len(B)
    cIndex = 0 #c = combined
    for num in B:
        if B.index(num) == 0:
            combined[B.index(num)] = insertNum(A, num)
        else:
            combined[B.index(num)] = insertNum(combined[cIndex], num)
            cIndex += 1
        #print ("WHOOP", num)
    print (combined[-1])