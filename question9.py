"""Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found."""

inputList = []
inputNum = int(input("Enter Number of sequence to be in List:  "))

for i in range(inputNum):
    inputItems = int(input("Enter item in List: "))
    inputList.append(inputItems)

sortedList = sorted(inputList)
print("-----------------------------------")
item = int(input("Enter item to be found: "))
print("-----------------------------------")

def binarySearch(sortedList, item):  

    firstItem = 0
    lastItem = len(sortedList)
    found = False
    index = -1
    
    while lastItem >= firstItem and not found:
        midItem = (firstItem+lastItem)//2

        if item > sortedList[midItem]:
            firstItem = midItem + 1
        elif item < sortedList[midItem]:
            lastItem = midItem-1 
        else:
            found = True
            index = midItem      

    return index

print("Found? ", binarySearch(sortedList, item))
        
