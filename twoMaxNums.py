"""
For a sequence of integers, find the biggest number
And the second biggest number without using a built-in function
(i.e. max(), sort())
"""
def twoMaxNums(listV = [3445, 5643, 2345, 9902, 3423, 1245, 4562]):
    if len(listV) < 2:
        print ("The length of your list is too small.")
        return

    maxNum1 = listV[0] #biggest
    maxNum2 = listV[1] #2nd biggest

    for num in listV: #iterate through the function
        if num > maxNum2:
            if num > maxNum1:
                maxNum1 = num
            else:
                maxNum2 = num

    print ("The largest num in the sequence %s is %a." %(listV, maxNum1))
    print ("The second largest num in the sequence %s is %a." %(listV, maxNum2))

#call the funcs
twoMaxNums()