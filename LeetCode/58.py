'''
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

# 8:06 start set up
# 8:11 start solving

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in s:
            if char == " ":
                length = 0
            else:
                length += 1
        return length
    
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        last_word_met = False
        for char in reversed(s) : 
            if char != " ":
                length += 1
                last_word_met = True
            if char == " " and last_word_met == True:
                return length