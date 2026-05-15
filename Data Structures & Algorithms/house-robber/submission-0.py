class Solution:
    def rob(self, nums: List[int]) -> int:
        # iterate through each house. 
        # let opt be the maximum amount of money you can make from houses
        #0 to i.

        # at any given point, lets say you are at index 5. 
        # you can choose, 5, 3, 1,
        # 4, 2
        #

        #what do i need to know at i? From the previous steps?
        # the max value including house n -1? The max value containing 
        # n -2? 

        if len(nums) <= 1:
            return nums[0]

        dp = [0] *( len(nums) + 1)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i -2] + nums[i])

        return dp[len(nums) - 1]