"""
For example,
the list is [6, 8, 10], insert number 7 to the list.

Note: Please do not use the embedded python method
for the insertion. You can use len(list).
"""
def insertNum(lst, numTI): #numI - num to insert
    index = 0
    for i in range (0, len(lst)):
        #print ("here0.5")
        #print (lst[i], numTI)
        if lst[i] < numTI:
            #print ("here0.75")
            if i != len(lst)-1:
                #print ("here")
                if lst[i+1] > numTI:
                    index = i
                elif lst[i+1] == numTI:
                    index = i+1
                    #print ("here2")
            else:
                index = i

    newList = [None] * (len(lst)+1)
    after = False
    for i in range (0, len(lst)+1):
        if i == index: #index+1?
            newList[i] = numTI
            after = True
        elif after:
            newList[i] = lst[i-1]
        else:
            newList[i] = lst[i]

    return newList