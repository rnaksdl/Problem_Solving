'''
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern
and a non-empty word in s.
'''

class Attempt:
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
