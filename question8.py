"""Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime."""


def is_prime():
    count = 0
    inputNumber = int(input("Enter an integer: "))

    for i in range(1, inputNumber):
        if inputNumber % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

print("Number is Prime ", is_prime())

