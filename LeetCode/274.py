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
    
class Solution2:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        h_index = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index
'''
this approach was really outside of the box
I need to think about sorting in decending order..

SO the way this solutions works is beautifully simple.
1. sort the array in decending order
2. initialize h index to 0
3. iterate thru the array
    1. if citation is greater than position in array (i + 1),
        1. set h index to the position in array (i + 1)
    2. else break the loop, since the numbers will be keep getting smaller anyway.
4. return the array.
'''