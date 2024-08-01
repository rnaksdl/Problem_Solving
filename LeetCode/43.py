'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Attempt1:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(1, len(height) - 2):
            left = height[i-1]
            bottom = height[i]
            right = height[i+1]

            water = min(left, right) - bottom
            if water >= 0:
                result += water

        return result
    
'''
this only checks for 1 depth holes..
'''
            