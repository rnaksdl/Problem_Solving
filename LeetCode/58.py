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