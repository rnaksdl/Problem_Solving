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


