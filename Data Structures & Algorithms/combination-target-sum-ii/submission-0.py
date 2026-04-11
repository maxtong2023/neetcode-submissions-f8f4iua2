class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        def backtrack(start, path, total):
            if total == target: 
                result.append(list(path))
                return

            if total > target: 
                return
            curr = ''
            for i in range(start,len(candidates)):
                if candidates[i] == curr: 
                    continue
                curr = candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return result
