class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <=1: 
            return cost[0]
        
        dp = [0] * (len(cost ) + 1)

        dp[0] = 0 # the cost it takes to just stay at the current element
        dp[1] = 0 # the cost it takes to make it to the very next element. 

        # the cost of dp[2] would be the minimum of dp[0] + cost[0] and dp[1] + cost[1]
        # or dp[n] = min(dp[n - 1] + cost[n-1], dp[n-2] + cost[n-2])

        for n in range(2, len(cost) + 1):
            dp[n] = min(dp[n - 1] + cost[n-1], dp[n-2] + cost[n-2])
        return dp[len(cost)]