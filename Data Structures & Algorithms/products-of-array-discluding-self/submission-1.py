class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val = 1 
        leftarray = [0] * len(nums)

        for i in range(len(nums)):
            leftarray[i] = val 
            val *= nums[i]
        
        val = 1 
        rightarray = [0] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            rightarray[i] = val
            val *= nums[i]
        result = []
        for i in range(len(nums)): 
            result.append(rightarray[i] * leftarray[i])
        
        return result
