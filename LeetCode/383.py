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