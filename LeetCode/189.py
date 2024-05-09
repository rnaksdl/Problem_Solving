'''
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''


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