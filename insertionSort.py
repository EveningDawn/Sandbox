def insertionSort(lst):
    resList = [None] * len(lst) #create the final list with the number of empty spaces
    resList[0] = lst[0] #assign something to the first spot in the list

    lstI = 1
    resI = -1
    for i in range (1, len(lst)):
        try:
            while lst[lstI] < resList[resI]:
                resI -= 1
                print ("resI: %s" %resI)
                continue
            else:
                print ("Hooray. lstI: %s, resI: %s" %(lstI, resI))
                resList[resI] = lst[lstI]
                print ("resList: %ls" %resList)
                lstI += 1
        except IndexError:
            print ("An IndexError has occured. lstI: %s, resI: %s" %(lstI, resI))
            print ("resList: %ls" %resList)
            return

    print (resList)

#call
insertionSort([1, 3, 5, 4])