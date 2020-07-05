"""Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age."""


# inputTuple1 = ('Gaurab', 'Dawadi', 22)
# inputList = []
# inputList.append(inputTuple1)
# print(inputList)

# fname = 'ram'
# lname = 'dawadi'
# age = 48
# inputTuple2 = (fname, lname, age)
# print(inputTuple2)

inputList = []

while (1):
    def createTuple():
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        age = int(input("Enter age: "))

        inputTuple = (firstName, lastName, age)

        return inputTuple

    inputList.append(createTuple())
    print(inputList)
    moreAdd = input("Do you want to add more (Y/N): ") 

    if moreAdd == 'Y':
        continue
    elif moreAdd == 'N':
        break   

#For default sorting i.e First Name   
# sortedList = sorted(inputList)

#For caustomized sorting / sorting by fields
sortedBylastName = sorted(inputList, key= lambda x: x[1])
print(sortedBylastName)

# sortedByAge = sorted(inputList, key= lambda x: x[2])
# print(sortedByAge)

