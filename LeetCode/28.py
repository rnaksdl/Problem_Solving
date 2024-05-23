'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''

class Attempt1:
    def strStr(self, haystack: str, needle: str) -> int:
        
        start = -1
        progress = 0
        
        for i, char in enumerate(haystack):
            if char == needle[progress]:
                progress += 1
                if start == -1:
                    start = i
            
            if progress == len(needle) - 1:
                return start
            
            if char != needle[progress]:
                progress = 0
                start = -1
                
        return -1
'''
over compelecated for sure..
'''


class Attempt2:
    def strStr(self, haystack: str, needle: str) -> int:
        
        progress = 0
        i = len(haystack) - 1
        j = len(needle) - 1
        
        while i > 0:
            if haystack[i] == needle[j]:
                progress += 1
                if progress == len(needle):
                    return i
                continue
            else:
                progress = 0
            
            i -= 1
            j -= 1
            
        return -1
'''
ugh I should not reverse it,
since I need to find the first occurrence
'''

class Attempt3:
    def strStr(self, haystack: str, needle: str) -> int:
        
        start = -1
        progress = 0
        
        for i, char in enumerate(haystack):
            if char == needle[progress]:
                progress += 1
                if start == -1:
                    start = i
                if progress == len(needle):
                    return start
                continue
            
            else:
                start = -1
                progress = 0
        
        return -1
'''
Input
"mississippi"
"issip"

Output
-1

Expected
4
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0
        
        # Length of needle and haystack
        n, m = len(haystack), len(needle)
        
        # Iterate over the haystack with a sliding window the size of the needle
        for i in range(n - m + 1):
            # Check if the substring of haystack starting at i matches needle
            if haystack[i:i + m] == needle:
                return i
        
        # If no match is found, return -1
        return -1
'''
wow....
really weird solution.
I'm glad I attempted this question.
This was very out of my knowledge.
'''