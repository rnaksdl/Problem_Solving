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
'''