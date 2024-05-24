'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

class Attempt:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        L = 0
        R = 0
        total = nums[0]
        length = len(nums) + 1
        
        while(L < len(nums) - 1 and R < len(nums)) - 1:
            print(L)
            print(R)
            if total >= target:
                if length > R - L + 1:
                    length = R - L + 1
                total -= nums[L]
                L += 1
                
            if total <= target:
                R += 1
                total += nums[R]
        
        if length == len(nums) + 1:
            return 0
        
        return length
                
'''
several issues here
I need to study sliding window a little more
'''

