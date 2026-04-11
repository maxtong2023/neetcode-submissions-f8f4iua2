class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxprofit = 0

        for i in prices: 
            lowest = min(lowest, i)
            maxprofit = max(maxprofit, i - lowest)
        return maxprofit

        

        