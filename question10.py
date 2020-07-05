"""Write a function that takes camel-cased strings (i.e.
ThisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well."""

import re

inputString = input("Enter string in camel-cased: ")

def camelCasedToSnakeCased(inputString):
    convert = re.sub('(?!^)([A-Z]+)', r'_\1', inputString).lower()
    return convert

print("This is Snake Cased: ", camelCasedToSnakeCased(inputString))

def camelCasedToKebabCased(inputString ):
    convert = re.sub('(?!^)([A-Z]+)', r'-\1', inputString).lower()
    return convert

print("This is Kebab Cased: ", camelCasedToKebabCased(inputString))


# inputString = input("Enter string in camel-cased: ")

# def camelCasedToSnakeCased(inputString):
#     newString = ''
#     if inputString[0].isupper():
#         newString = newString + inputString[0].lower()

#     for i in range(1, len(inputString)):       
#         if inputString[i].islower():
#             newString = newString + inputString[i]
#         else:
#             newString = newString + '_'  + inputString[i].lower()                 
#     return newString

# print("This is Snake Cased: ", camelCasedToSnakeCased(inputString))

# def camelCasedToKebabCased(inputString):
#     newString = ''
#     if inputString[0].isupper():
#         newString = newString + inputString[0].lower()

#     for i in range(1, len(inputString)):       
#         if inputString[i].islower():
#             newString = newString + inputString[i]
#         else:
#             newString = newString + '-'  + inputString[i].lower()                 
#     return newString

# print("This is Kebab Cased: ", camelCasedToKebabCased(inputString))


##Using Regular Expression




