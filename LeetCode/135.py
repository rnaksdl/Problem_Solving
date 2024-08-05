'''
135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
'''


class Attempt1:
    def candy(self, ratings: List[int]) -> int:

        result = 0

        for i in range(len(ratings)):
            result += 1

            if i == 0:
                if ratings[i] > ratings[i + 1]:
                    result += 1

            if i == len(ratings) - 1:
                if ratings[i] > ratings[i - 1]:
                    result += 1

            if i > 0 and i < len(ratings)-1:
                if ratings[i] > ratings[i - 1] or ratings[i] > ratings[i + 1]:
                    result += 1

        return result
'''
Children with a higher rating get more candies than their neighbors
'''
    

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # init array with the length of ratings, filled with 1's
        arr = [1] * len(ratings)
        
        # skip the first ele and iter
        for i in range(1, len(ratings)):
            # if prev less than current
            if ratings[i - 1] < ratings[i]:
                # update the arr value
                arr[i] = arr[i - 1] + 1

        # skip the last ele and iter backwards
        for i in range(len(ratings) - 2, -1, -1):
            # if current greater than prev
            if ratings[i] > ratings[i + 1]:
                # up date the arr value
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)