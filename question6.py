"""Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it."""

foundCount = 0
inputNum = int(input("Enter Number of names you want: "))

inputList = [input("Enter a Name of Collegue or Friend: ").title() for i in range(inputNum)]

for name in inputList:
    if name == 'John':
        foundCount += 1    
        
if foundCount >= 1:
    print("Found")
else:
    print("Not Found")     
               
    