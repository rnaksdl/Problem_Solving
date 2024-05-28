'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring
 without repeating characters.
 '''

class Attempt:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # initialize dict
        dict = {}

        # init Left pointer and maxLength
        L = 0
        maxLength = 0

        # iter each char in s
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
                print(dict)
                currentLength = i - L + 1
                if maxLength < currentLength:
                    maxLength = currentLength
            elif s[i] not in dict:
                dict.pop(s[L])
                print(dict)
                L += 1


        return maxLength
'''
doesn't remove char in out of range
'''

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])

            currentLength = r - l + 1
            if maxLength < currentLength:
                maxLength = currentLength

        return maxLength
'''
sliding window with set

there are some other solutions but this one is simple and efficient.
'''