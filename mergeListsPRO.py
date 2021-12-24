"""
Given two lists of numbers in increasing order,
merge the two lists into one list in increasing order.
For example, [3, 6, 9] and [2, 5, 7] will merge into [2, 3, 5, 6, 7, 9].
Please note, no embedded Python functions are allowed to use.
You have to write your own functions to do this.
"""

def mergeListsPRO(list1, list2):
    l = len(list1) + len(list2)
    final = [None] * l #get empty spaces

    #vars
    l1i, l2i, fi = 0, 0, 0
    #l1i is for list1 index; same for the others

    while fi < l: #until the full list capacity is reached
        try:
            if l1i >= len(list1): #don't want to get IndexError
                for i in range (l2i, len(list2)): #append all
                    final[fi] = list2[i]
                    fi += 1
                break
            if l2i >= len(list2): #same as line 19
                for i in range (l1i, len(list1)): #append all
                    final[fi] = list1[i]
                    fi += 1
                break

            if list1[l1i] <= list2[l2i]: #compare
                final[fi] = list1[l1i] #put it in final
                l1i += 1 #update var
                fi += 1 #update var
            else:
                final[fi] = list2[l2i] #put it in final
                l2i += 1 #update var
                fi += 1 #update var
        except IndexError:
            print ("IndexError - f1: %s, l1i: %s, l2i: %s" %(fi, l1i, l2i))
            print ("Final: %ls" %final)
            return

    print (final)

#call
mergeListsPRO([3, 6, 9], [2, 5, 7])
mergeListsPRO([1, 2, 678, 932], [3, 10, 12, 837, 2021, 3001, 3002])