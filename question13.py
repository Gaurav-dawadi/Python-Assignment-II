"""Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple."""

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
print("name, address, age")
for i in gotBack:
    print('%s, %s, %s' %i)





