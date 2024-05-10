




NOT DONE YET




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