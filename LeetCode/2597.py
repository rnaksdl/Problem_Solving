'''
2597. The Number of Beautiful Subsets
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained
by deleting some (possibly none) elements from nums.
Two subsets are different if and only if
the chosen indices to delete are different.
'''

class Attempt:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        sol = set()
        
        for n in nums:
            sol.add(n)
            for m in nums:
                if abs(n - m) == k:
                    continue
                if n < m:
                    sol.add((n, m))
                elif m < n:
                    sol.add((m, n))
        
        print(sol)
        return len(sol)
    
'''
only checks two numbers
'''

