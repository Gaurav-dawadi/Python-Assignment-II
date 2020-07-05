"""Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?"""


print("------------------------------------------------")
print("!!!!!!!!Info Of Customer For New Account Creation!!!!!!!!")
inputName = input("Enter Name of customer: ")
inputAge = int(input("Enter Age of customer: "))
inputOccupation = input("Enter Occupation of customer: ")
inputSalary = int(input("Enter Salary of customer: "))
print("------------------------------------------------")

class Customer:

    def __init__(self, name, age, occupation, salary):
        self.name = name.title()
        self.age = age
        self.occupation = occupation.title()
        self.salary = salary


    def total_deposited_amount(self, time_in_year = 2, rate=0.01):
        # deducted_money = self.money_withdrawned()
        totalSavings = self.salary + ((self.salary*0.01)*time_in_year)
        return totalSavings

    def money_deposited_recently(self):
        return self.salary

    def money_withdrawned(self):
        totalAmountInAccount = self.total_deposited_amount() 
        money_to_be_withdrawn = input("Enter money you want to withdraw: ")
        if float(money_to_be_withdrawn) < totalAmountInAccount:
            withdrawn = money_to_be_withdrawn
            return withdrawn
        else:
            return "You donot have Sufficient money to withdraw" 


infoCustomer = Customer(inputName, inputAge, inputOccupation, inputSalary)
print("!!!! Info Of A Acoount Holder !!!!")
print("Name of Customer: ", infoCustomer.name)
print("Total Amount in Bank After One Year: ", infoCustomer.total_deposited_amount())
print("Money Deposited Recently: ", infoCustomer.money_deposited_recently())
print("Money Withdrawn Recently: ", infoCustomer.money_withdrawned())
print("------------------------------------------------------")              
