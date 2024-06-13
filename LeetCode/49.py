'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''





class Attempt:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        for word in strs:
            sorted(word)

        sorted(strs)

        result = []
        temp = []

        for i in range(len(strs) - 1):
            if strs[i] == strs[i - 1]:
                temp.append
'''
I was lost in this one.
'''

