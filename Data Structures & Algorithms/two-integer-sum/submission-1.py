class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i in range(len(nums)):
            if index.get(nums[i]) != None:
                return [index[nums[i]], i]
            else:
                index[target - nums[i]] = i
        return