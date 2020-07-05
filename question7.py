"""Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age."""

inputList = []

while (1):
    def createTuple():
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        knowAge = input("Do you Know age of your Friend (Y/N)")
        if knowAge == 'Y':
            age = int(input("Enter age: "))
        elif knowAge == 'N':
            age = None
        
        inputTuple = (firstName, lastName, age)
        return inputTuple

    inputList.append(createTuple())
    print(inputList)
    moreAdd = input("Do you want to add more (Y/N): ") 

    if moreAdd == 'Y':
        continue
    elif moreAdd == 'N':
        break 

sumOfAge = 0
countOfAge = 0
for i in inputList:
    if i[-1] != None:
        sumOfAge += i[-1]
        countOfAge += 1
   
print("The sum of Age: ", sumOfAge)
averageAge = sumOfAge//countOfAge

for items in inputList:
    takeName = items[0]  
    takeAge = items[-1]

    if takeAge != None:
        if takeAge>averageAge:
            print("{} is Old".format(takeName))
        else:
            print("{} is Young".format(takeName))



