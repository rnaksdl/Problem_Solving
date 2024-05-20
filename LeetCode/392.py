'''
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        
        if len(s) == 0:
            return True
        
        for char in t:
            if s[i] == char:
                i += 1
            if i == len(s):
                return True

        return False
    
'''
Got it in first try?!?!

BUT I didn't use two poiters..
'''


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        s_pointer, t_pointer = 0, 0
        
        # Iterate through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If characters match, move the pointer for s
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            # Always move the pointer for t
            t_pointer += 1
        
        # If we have traversed all characters in s, it is a subsequence of t
        return s_pointer == len(s)
