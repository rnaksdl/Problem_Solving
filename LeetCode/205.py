'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.
No two characters may map to the same character,
but a character may map to itself.
'''


class Attempt1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # if not s or not t:
        #     return False

        # if len(s) != len(t):
        #     return False

        dictionary = {}
        
        for i in range(len(s)):
            if dictionary.get(s[i]) != t[i]:
                return False
            
            dictionary[s[i]] = t[i]

        return True


class Attempt2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # if not s or not t:
        #     return False

        # if len(s) != len(t):
        #     return False

        charDict = {}
        
        for i in range(len(s)):
            if s[i] in charDict and charDict.get(s[i]) != t[i]:
                return False
            
            charDict[s[i]] = t[i]

        return True
'''
it should go both ways
'''



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}
        
        for i in range(len(s)):
            if s[i] in sDict and sDict[s[i]] != t[i]:
                return False
            
            if t[i] in tDict and tDict[t[i]] != s[i]:
                return False

            
            sDict[s[i]] = t[i]
            tDict[t[i]] = s[i]

        return True
