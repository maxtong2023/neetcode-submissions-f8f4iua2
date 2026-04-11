class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, path, total):
            if total == target: 
               
                result.append(list(path))
                return

            if total > target: 
                return 

            for i in range(start, len(nums)):
                # add to the path
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()

        backtrack(0, [], 0 )
        return result

            

