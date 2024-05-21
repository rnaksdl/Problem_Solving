'''
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p1 = 0
        p2 = len(numbers) - 1
        
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1