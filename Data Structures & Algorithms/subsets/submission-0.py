class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []

        def backtrack(start, currentpath):
            results.append(list(currentpath))

            for i in range(start, len(nums)):
                currentpath.append(nums[i])
                backtrack(i + 1, currentpath)
                currentpath.pop()
        backtrack(0, [])
        return results
        