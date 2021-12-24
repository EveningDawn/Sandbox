"""
Given two lists of numbers in increasing order,
merge the two lists into one list in increasing order.
For example, [3, 6, 9] and [2, 5, 7] will merge into [2, 3, 5, 6, 7, 9].
Please note, no embedded Python functions are allowed to use.
You have to write your own functions to do this.
"""

def mergeLists(list1, list2):
    l = len(list1) + len(list2) #find the number of empty spaces
    #needed to use in line 13

    final = [None] * l #create empty spaces for each part of the list
    #line 13 is necessary because you cannot use .append()
    #since .append() is an embedded Python function

    for i in range (len(list1)):
        final[i] = list1[i] #add each element in list1 into the final list

    for i in range (len(list1), len(list1) + len(list2)): #so that the index starts
        #after list1 so that it adds the element in the right place
        final[i] = list2[i - len(list1)] #adding the element

    return final

def leastToGreatest(lst):
    final = [None] * len(lst) #create a new list for the final result

    #print ("Original list: %ls" %lst)
    for i in range (len(lst)): #go through every element in the list
        minNum = findMinNum(lst)
        #print ("minNum: %s, i: %s" %(minNum, i))
        final[i] = minNum
        #print ("final (the list): %ls" %final)
        lst = removeNum(lst, minNum) #so it doens't get the same number again
        #print ("lst (after minNum removed): %ls" %lst)

    print (final)

def findMinNum(lst): #this will help with the leastToGreatest()
    minNum = 100000000 #make something really big

    for num in lst: #go through every number in the list
        if num < minNum: #inequality
            minNum = num #set new min

    return minNum

def removeNum(lst, rmv):
    i = lst.index(rmv)
    multi = len(lst) - 1
    res = [None] * multi #create empty spaces

    for x in range(len(lst)): #for loop
        if rmv != lst[x]: #if it's not the one you want to get rid of
            if x > i: #to get rid of having None in the list
                res[x-1] = lst[x]
            else:
                res[x] = lst[x]

    lst = res
    return lst

#call
lst = mergeLists([3, 6, 9], [2, 5, 7])
leastToGreatest(lst)
#findMinNum(lst)