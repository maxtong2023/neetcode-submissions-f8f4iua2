class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()

        def backtrack(start, path): 
            sortpath = tuple(sorted(path))
            if sortpath not in seen: 
                

                result.append(path[:])
                seen.add(sortpath)
                
  
            for i in range(start, len(nums)): 
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0,[])
        return result

