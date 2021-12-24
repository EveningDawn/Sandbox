"""
Given a list of numbers, and a target number,
Output the indices of the two numbers whose addition is the target number.
If no such two numbers exist, output none.
"""
def addendsAndIndicies(numList = [14, 5, 7, 6, 9, 12], targetNum = 11):
    for num in numList:
        for num2 in numList:
            if num + num2 == targetNum:
                addend1 = num
                addend2 = num2
                print ("The first addend is %a." %addend1)
                print ("The index of the first addend is %a." %numList.index(addend1))
                print ("The second addend is %a." %addend2)
                print ("The index of the second addend is %a." %numList.index(addend2))
                return
    print ("No such pairs exist in the list.")

def addendsAndIndicies_v2(numList = [14, 5, 7, 6, 9, 12], targetNum = 11):
    for num in range (len(numList)):
        otherAddend = targetNum - numList[num]
        if otherAddend in numList:
            print ("The first addend is %a." %numList[num])
            print ("The index of the first addend is %a." %num)
            print ("The second addend is %a." %otherAddend)
            print ("The index of the second addend is %a." %numList.index(otherAddend))
            return

#call the funcs
addendsAndIndicies()
print ("\n")
addendsAndIndicies_v2()