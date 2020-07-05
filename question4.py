"""Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?"""

inputList = []
print("The id of List is ",id(inputList))
print("--------------------------------")

inputNum = int(input("Enter the number of Names you want to input: "))

for i in range(inputNum):
    inputFriend = input("Enter the Name of your Friend or Collegues: ")
    inputList.append(inputFriend)

print("The id of List is ", id(inputList))
print("--------------------------------")

print("NO the Id hasnot changed")

sortedList = sorted(inputList)
print("--------------------------------")
print("The first item in List is ", sortedList[0])
print("The second item in List is ", sortedList[1])
print("--------------------------------")




