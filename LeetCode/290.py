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