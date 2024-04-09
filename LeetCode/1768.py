'''
1768. Merge Strings Alternately
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''

# this solution only works when word2 is longer
class Attempt1:
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
    
# fixed the attepmt1's issue by checking which one's longer and handling them differently in each case
class Attempt2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        position = 0
        result = ""
        
        if len(word1) >= len(word2):
            for i, char in enumerate(word2):
                result += word1[i]
                result += word2[i]
                position += 1
            for i in range(position, len(word1)):
                result += word1[i]
            return result
        
        if len(word1) < len(word2):
            for i, char in enumerate(word1):
                result += word1[i]
                result += word2[i]
                position += 1
            for i in range(position, len(word2)):
                result += word2[i]
            return result