'''
1768. Merge Strings Alternately
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''


# 5:18 start
# 5 19 done setup
# 5:25 first attempt

# this solution only works when word2 is longer
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        position = 0
        result = ""
        
        while position < len(word1):
            result += word1[position]
            result += word2[position]
            position += 1
        
        while position < len(word2):
            result += word2[position]
            position += 1
        
        return result