'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check lenths
        if len(s) != len(t):
            return False

        # init dicts
        sDict = {}
        tDict = {}

        # iter length
        for i in range(len(s)):

            # if char isn't in the dicts, init
            if s[i] not in sDict:
                sDict[s[i]] = 0
            if t[i] not in tDict:
                tDict[t[i]] = 0
            
            # increment
            sDict[s[i]] += 1
            tDict[t[i]] += 1

        return sDict == tDict
'''
this was very easy to me
got it in my first try.. that doesn't happen often
'''