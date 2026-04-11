class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]

        current_sum= 0
        for i in nums: 
            current_sum = max(i, current_sum+ i)
            global_sum = max(global_sum, current_sum)
        return global_sum


        