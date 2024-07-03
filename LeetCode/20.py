'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Attempt1:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            if char == ")":
                if stack.pop() != "(":
                    return False
            if char ==  "}":
                if stack.pop() != "{":
                    return False
            if char ==  "]":
                if stack.pop() != "[":
                    return False
        
        if len(stack) != 0:
            return False
        return True
'''
I'm close...
I feel sick tho, so I can't think straight..
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen [c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        