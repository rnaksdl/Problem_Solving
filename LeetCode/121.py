'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
		# initiallizing the buying price to a large number
        bought_at = 10000000
        # initiallizing the max profit to a small number
        max_profit = 0
        
		# iterate through the list of prices
        for price in prices:
            # if cheaper price found, update buying price
            if price < bought_at:
                bought_at = price
            # profit = price - bought_at
            # if greaterprofit found, update max profit value
            if price - bought_at > max_profit:
                max_profit = price - bought_at
        
        return max_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))