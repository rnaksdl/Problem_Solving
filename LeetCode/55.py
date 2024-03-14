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
        
solution1 = Solution1()
print(solution1.canJump([2,3,1,1,4]))


"""
More efficient way
I learned about range(start, stop, step)
This approach goes througth the array backwards and updates the goal if it's reachable.
"""

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1 , -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
    
solution2 = Solution2()
print(solution2.canJump([2,3,1,1,4]))