'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

from typing import List

'''
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i = 0
        commonPrefixString = strs[0][0]
        counter = 0;
        
        while true:
            
            for str in strs:
                
                if str[i] == commonPrefixString:
                    counter += 1
                else:
                    counter -= 1
                if counter < 0:
                    commonPrefixString = str[i]
            i += 1

I realized that I misunderstood the problem midway of attempt1.
We are looking for 'COMMON' prefix, which means all strings should have some same prefix.
'''

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        commonPrefix = ""
        
        strings = sorted(strs)
        
        for i in range(len(strings[0])):
            if strings[0][i] == strings[-1][i]:
                commonPrefix += strings[0][i]
            else:
                return commonPrefix

"""
attempt2 doesn't catch the edge case of the list being empty
"""



class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        strings = sorted(strs)
        firstS=strings[0]
        lastS=strings[-1]
        for i in range(min(len(firstS),len(lastS))):
            if(firstS[i]!=lastS[i]):
                return commonPrefix
            commonPrefix += firstS[i]
        return commonPrefix