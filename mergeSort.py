"""
Give a list of numbers, sort them with the merge sort algorithm:

MergeSort(arr[], l, r)
If r > l
    1. Find the middle point to divide the array into two halves:
            middle m = (l+r)/2
    2. Call mergeSort for first half:
            Call mergeSort(arr, l, m)
    3. Call mergeSort for second half:
            Call mergeSort(arr, m+1, r)
    4. Merge the two halves sorted in step 2 and 3:
            Call merge(arr, l, m, r)

In other words...
Given a list of numbers, divide them until they're single. Then, use the merge
sort algorithm to merge them, two and two until it becomes one list again.
"""

def mergeSort(lst, startIndex, endIndex):
    if endIndex > startIndex:
        middle = (startIndex + endIndex) / 2 #find the middle
        mergeSort(lst, startIndex, middle) #use recursion to spilt the list into two
        mergeSort(lst, middle + 1, endIndex) #same as above; this is second half
        merge(lst, startIndex, middle, endIndex) #combiniation process
        print (lst)

def merge(lst, startIndex, middle, endIndex):
    list1 = [None] * (middle - startIndex + 1) #create list1
    list2 = [None] * (endIndex - middle) #create list2

    j = 0 #var
    for i in range (startIndex, middle + 1): #for loop to
        list1[j] = lst[i] #add things to the list
        j += 1
    j = 0 #reset back to 0
    for i in range (middle + 1, endIndex + 1): #for loop to
        list2[j] = lst[i] #add things to the list
        j += 1

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

    j = 0
    for i in range (startIndex, endIndex + 1): #moving everything from final to lst
        lst[i] = final[j]
        j += 1

    return lst

#call
lst = [3, 1, 6, 4, 8, 2, 5, 4]
mergeSort(lst, 0, 7)