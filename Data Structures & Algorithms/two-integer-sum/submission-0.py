class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash ={}
        difference = 0
        for i in range(len(nums)):
            difference = target - nums[i]
            if(numhash.get(nums[i]) != None):
                return [numhash.get(nums[i]), i]
            numhash[difference] = i
        

            

        