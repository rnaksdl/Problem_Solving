'''
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''


from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        k is the rotate point
        which means first element goes to k
        """
        
        swap_value = nums[0]
        
        for i in range(len(nums)//2):
            
            swap_value = nums[0 + i]
            
            nums[0] = nums[k]
            
            nums[k + i] = swap_value


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        k is the rotate point
        which means first element goes to k
        """
        newNums = []
        
        for i in range(0, k+1):
            nums.append(nums[i])
        for i in range(0, k+1):
            del nums[0]




'''
This one works, BUT it isn't so efficient
it is very easy to understand this logic tho
1234567, 3
    append first 4 int
        12345671234
    delete first 4 int
        5671234
'''
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        k is the rotate point
        which means first element goes to k
        """
        
        for i in range(1, k+1):
            nums.insert(0, nums[-i])
            
        for i in range(1, k+1):
            del nums[-1]


'''
still not so fast
but less memory usage
'''
class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        k is the rotate point
        which means first element goes to k
        """
        
        for i in range(1, k+1):
            nums.insert(0, nums[-1])
            del nums[-1]