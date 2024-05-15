'''
122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''



from typing import List


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 0
        profit = 0
        
        for i in range(1, len(prices)):
            if buy == 0 and prices[i-1] < prices[i]:
                buy = prices[i-1]
            if buy != 0 and prices[i-1] > prices [i]:
                sell = prices[i-1]
                profit += sell - buy
                buy = 0
                
        return profit
'''
We must sell the stocks, we can't hold.
'''


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 0
        profit = 0
        
        for i in range(1, len(prices)):
            if buy == 0 and prices[i-1] < prices[i]:
                buy = prices[i-1]
            if buy != 0 and prices[i-1] > prices [i]:
                sell = prices[i-1]
                profit += sell - buy
                buy = 0
            if buy != 0 and i == len(prices) - 1:
                sell = prices[i]
                profit += sell - buy
                buy = 0
                
        return profit
'''
since we check if the buy is 0 as we are checking if we didn't buy
when we actually buy at 0
the algo assumes we didn't buy
'''