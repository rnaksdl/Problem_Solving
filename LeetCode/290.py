'''
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern
and a non-empty word in s.
'''

class Attempt1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        counter = 0
        word = ""
        wordDict = {}

        for char in s:
            if char == " ":
                counter += 1
                
                if pattern[counter] in wordDict and wordDict[pattern[counter]] != word:
                    return False
                wordDict[pattern[counter]] = word
                word = ""
        
        return True
'''
I'm definitely over thinking,
I need to get used to using two or more hashmaps.
'''

class Attempt2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        counter = 0
        word = ""
        w2p = {}
        p2w = {}

        for char in s:
            if char == " ":
                if word in w2p and w2p[word] != pattern[counter]:
                    return False
                if pattern[counter] in p2w and p2w[pattern[counter]] != word:
                    return False
                
                counter += 1

        return False
    

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = ""
        w2p = {}
        p2w = {}
        counter = 0
        s += ' '  # Add a space at the end to handle the last word

        for char in s:
            if char != " ":
                word += char  # Build the word character by character
            else:
                if counter >= len(pattern):  # Check if there are more words than pattern characters
                    return False
                if word in w2p and w2p[word] != pattern[counter]:
                    return False
                if pattern[counter] in p2w and p2w[pattern[counter]] != word:
                    return False
                w2p[word] = pattern[counter]
                p2w[pattern[counter]] = word
                word = ""  # Reset word for the next iteration
                counter += 1  # Move to the next pattern character

        # After processing all characters, check if all pattern characters were used
        return counter == len(pattern)
'''
Runtime
36
ms
Beats
47.25%
of users with Python3
Memory
16.36
MB
Beats
98.78%
of users with Python3
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # parse string
        words = s.split(" ")

        # check lengths
        if len(pattern) != len(words):
            return False
        
        # init two dicts
        c2w = {}
        w2c = {}

        # iter both same time
        for c, w in zip(pattern, words):

            # check if c already exists and has same w
            if c in c2w and c2w[c] != w:
                return False
            
            # check if w already exists and has same c
            if w in w2c and w2c[w] != c:
                return False

            # add w, c to each dicts
            c2w[c] = w
            w2c[w] = c

        return True

