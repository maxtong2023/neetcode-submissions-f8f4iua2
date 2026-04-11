class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumps = 0
        maxreach = 0 
        window = 0


        for i in range(goal):
            maxreach = max(maxreach, nums[i] + i)

            # we've reached the subwindow
            if i == window:
                jumps+=1
                window = maxreach
        return jumps

            


        