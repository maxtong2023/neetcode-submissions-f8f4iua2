class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        def iterate(sublist):
            if len(sublist) <= 1: 
                return nums[0]
            dp = [0] * (len(sublist) + 1)
            dp[0] = sublist[0]
            dp[1] = max(sublist[0], sublist[1])

            for i in range(2, len(sublist)):
                dp[i] = max(dp[i - 1], dp[i -2] + sublist[i])
            return dp[len(sublist) - 1]

        return max(iterate(nums[1:]), iterate(nums[:-1]))