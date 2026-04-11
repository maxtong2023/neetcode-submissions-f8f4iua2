class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # being able to land on something like 4 means that you can choose 
        # to jump 1 2 3 or 4. 

        # basically, I'm thinking take a greedy approach. On the current element
        # you are on, take subarray that you can form for example if the first 
        # element you are on is a 2, the subarray will be the next two elements. 
        # if the element you are on + the index is greater than the length of the 
        # whole array, return true. 

        # otherwise, pick the max value out of that subarray and repeat the process. 

        goal = len(nums)- 1
        maxreach = 0

        for i in range(len(nums)):
            if i > maxreach: 
                return False
            
            maxreach = max(maxreach, i + nums[i])

            if maxreach >= goal:
                return True
        return False
        