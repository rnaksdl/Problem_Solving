'''
274. H-Index
Given an array of integers citations where
citations[i] is the number of citations a researcher received for their ith paper,
return the researcher's h-index.

According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h
such that the given researcher has published at least h papers
that have each been cited at least h times.
'''


from typing import List


class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        
        for i in citations:
            count = 0
            result = 0
            for j in citations:
                if citations[i] <= citations[j]:
                    count += 1
                if count > citations[i] and result < count:
                    result = count
            
            count = 0
                
        return result
'''
I could not come up with a working solution
'''
