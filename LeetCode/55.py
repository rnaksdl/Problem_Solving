'''
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
'''

from typing import List

"""
My first attempt was to actually jump through the array, but it was inefficient.
"""
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        pos = 0 
        
        while pos < len(nums) - 1:
            pos += nums[i]
            i = pos
            
        if pos == len(nums) - 1:
            return True
        else: return False
        
solution = Solution1()
print(solution.canJump([2,3,1,1,4]))


