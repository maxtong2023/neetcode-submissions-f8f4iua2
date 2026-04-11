class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # first impression is to just use a hashmap.

        # there is a better way you can solve this. 1:n will sum to a specific integer. 

        seen = set()

        for i in nums: 
            if i in seen: 
                return i
            else: 
                seen.add(i)
        