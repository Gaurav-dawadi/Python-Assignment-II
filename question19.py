"""Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid"""


class validity_of_string_parentheses:

   def valid_or_not(self, str1):
        aList, inputString = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in inputString:
                aList.append(parenthese)
            elif len(aList) == 0 or inputString[aList.pop()] != parenthese:
                return False
        return len(aList) == 0

print(validity_of_string_parentheses().valid_or_not("(){}[]"))
print(validity_of_string_parentheses().valid_or_not("()"))
print(validity_of_string_parentheses().valid_or_not("[)"))
print(validity_of_string_parentheses().valid_or_not("({[)]"))
print(validity_of_string_parentheses().valid_or_not("{{{"))
