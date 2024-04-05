'''
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

# took about 30 minutes to setup, attempt in 2 different ways, and check with other's solutions

# I honestly didn't read the description carefully and I didn't think of s ending in spaces..
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in s:
            if char == " ":
                length = 0
            else:
                length += 1
        return length
    
solution1 = Solution1()
print(solution1.lengthOfLastWord("   fly me   to   the moon  ") == 4)


# So I came up with this approach, which loops through s backwards and returns length when the word ends.
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
solution2 = Solution2()
print(solution2.lengthOfLastWord("   fly me   to   the moon  ") == 4)


# this is other's solution which is very similar to my approach, but using while loop, so it doesn't need "last_word_met = False" part.
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
solution3 = Solution3()
print(solution3.lengthOfLastWord("   fly me   to   the moon  ") == 4)