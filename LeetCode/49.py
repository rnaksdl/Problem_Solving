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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # init result hashmap
        result = defaultdict(list)

        # init 26 lists for a to z
        for word in strs:
            count = [0] * 26 

            # map char to each indices
            for char in word:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(word)

        return result.values()

'''
I don't think I would have been able to thought of this solution.
My first attempt was close to be another solution tho.
I'll study more about ord() and defualtdict()
'''