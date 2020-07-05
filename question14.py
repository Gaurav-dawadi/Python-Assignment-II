""" Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':'John', 'address': '54 Love Ave', 'age': 21}] """

inputList = []
def commaSeparatedValue():
    while 1:
        count = 1

        inputName = input("Enter your First Name: ")
        inputAddress = input("Enter your  Address: ")
        inputAge = int(input("Enter your Age: "))

        inputTuple = (inputName, inputAddress, inputAge)
        inputList.append(inputTuple)

        continueInput = input("Do you want to Add more info? (Y/N): ")
        if continueInput == 'Y':
            count += 1
            continue
        elif continueInput == 'N':
            break
    
    return inputList    

gotBack = commaSeparatedValue()
newList = []
for i in gotBack:

    dic = {}
    dic['name'] = i[0]
    dic['address'] = i[1]
    dic['age'] = i[2]
    newList.append(dic)

print(newList)
