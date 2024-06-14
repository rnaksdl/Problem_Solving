'''
45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums: List[int]) -> int:

        # init result, Left, Right to 0
        result = 0
        L = 0
        R = 0

        # iter till Right hasn't reached the end
        while R < len(nums) - 1:

            # init farthest to 0
            farthest = 0

            # iter Left to Right
            for i in range(L, R + 1):
                # set farthest to max of farthest or jump range
                farthest = max(farthest, i + nums[i])
            
            L = R + 1
            R = farthest
            result += 1

        return result