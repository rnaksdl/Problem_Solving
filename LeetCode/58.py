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
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                length += 1
                last_word_met = True
            elif last_word_met:
                return length
        return length
'''
Runtime: 38 ms, faster than 31.74% of Python3 online submissions for Length of Last Word.
Memory Usage: 16.4 MB, less than 98.65% of Python3 online submissions for Length of Last Word.
'''


class Solution3:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length
'''
Runtime: 42 ms, faster than 9.97% of Python3 online submissions for Length of Last Word.
Memory Usage: 16.6 MB, less than 27.02% of Python3 online submissions for Length of Last Word.
'''