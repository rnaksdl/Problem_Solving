'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''


class Attempt1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        val = 1
        for i in range(len(nums) - 1):
            result.append(val * nums[i])
            val = nums[i]

        val = 1
        for i in range(len(nums) - 1, -1, -1):
            result.append(val * nums[i])
            val = nums[i]

        return result


class Attempt2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]
        val = 1
        for i in range(len(nums) - 1):
            result.append(val * nums[i])
            val = nums[i]

        val = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= val
            val *= nums[i]

        return result
    
