"""Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed."""


inputWord = input("Enter any word to check Palindrome: ")

def is_palindrome(inputWord):

    reversedWord = inputWord[::-1]

    if inputWord == reversedWord:
        return ("The given word is Palindrome")
    else:
        return("The given word is not Palindrome") 

print(is_palindrome(inputWord))