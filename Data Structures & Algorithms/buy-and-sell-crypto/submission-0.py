class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bestprice = prices[0]
        profit = 0

        for i in range(len(prices)):
            if(bestprice > prices[i]):
                bestprice = prices[i]
            if(prices[i] - bestprice > profit):
                profit = prices[i] - bestprice
        return profit
        

        