'''
219. Contains Duplicate II

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Attempt:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        l = 0
        minDistance = 100000

        for r in range(len(nums)):
            while nums[r] in window:
                distance = r - l
                if minDistance > distance:
                    minDistance = distance
                else:
                    l = r

            window.add(nums[r])

            
        
        return True if distance <= k else False
    
'''
I'm still not understanding how sliding window works

I studied a bit,
and what I'm understanding so far is that
literally slide around the windoow according to the description
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # init window as set
        window = set()

        # init Left end of window
        L = 0

        # iterate nums
        for R in range(len(nums)):
            
            # window size should be <= k
            if R - L > k:
                
                # so remove first iten in window
                window.remove(nums[L])

                # and increment Left end of window
                L += 1

            # if new item is in window, return True
            if nums[R] in window:
                return True

            # add new item to window
            window.add(nums[R])
        
        # if it never returned True, return False
        return False
