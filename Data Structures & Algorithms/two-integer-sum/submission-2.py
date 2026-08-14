class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hasher = {}

        for i in range(len(nums)): 
            if nums[i] in hasher: 
                return [hasher[nums[i]], i]
            hasher[target - nums[i]] = i