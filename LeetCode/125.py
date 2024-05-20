'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for char in s:
            if char == "":
                char = ""
        print(s)
        for i in range(len(s) - 1):
            if s[i] != s[-i]:
                return False
            return True
'''
I need some hints...
'''

