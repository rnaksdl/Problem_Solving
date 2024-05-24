'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counter = {}
        
        for char in magazine:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                
        for char in ransomNote:
            
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
            
            if char not in counter:
                return False
            
            return True

'''
Doesn't pass this test:
Input
"fihjjjjei"
"hjibagacbhadfaefdjaeaebgi"
Output
true
Expected
false
'''


class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counter = {}
        
        for char in magazine:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                
        for char in ransomNote:
            
            if char not in counter:
                return False
            
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
            

            
        return True

'''
it was just a syntax error

Runtime: 58 ms, faster than 53.74% of Python3 online submissions for Ransom Note.
Memory Usage: 16.7 MB, less than 85.05% of Python3 online submissions for Ransom Note.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(ransomNote), Counter(magazine)
        
        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        if note & mag == note: return True
        return False
'''
Runtime: 55 ms, faster than 63.11% of Python3 online submissions for Ransom Note.
Memory Usage: 16.8 MB, less than 46.09% of Python3 online submissions for Ransom Note.
'''