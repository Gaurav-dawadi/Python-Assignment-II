''' Write an if statement to determine whether a variable holding a year is a leap year. '''


inputYear = int(input("Enter a Year: "))

if ((inputYear%400 == 0) or ((inputYear% 400 == 0) and (inputYear%100 == 0))):
    print("The Given Year is Leap Year")
else:
    print("The Given Year is not Leap Year")    