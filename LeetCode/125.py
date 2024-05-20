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

class Solution1:
    def isPalindrome(self, s: str) -> bool:

        # initialize an epmty array
        filtered_chars = []

        # iterate thru og array
        for char in s:
            
            # filter only alphnumericals
            if char.isalnum():

                # convert upper to lower case and append
                filtered_chars.append(char.lower())
        
        # initialize two pointers
        left = 0
        right = len(filtered_chars) - 1
        
        # iterate 
        while left < right:

            # array isn't palindrome
            if filtered_chars[left] != filtered_chars[right]:
                return False
            
            # moving poiters closer to middle
            left += 1
            right -= 1
        
        # is palindrome
        return True
