class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numhash ={}

        for i in nums: 
            if(numhash.get(i) != None):
                return True
            else:
                numhash[i] = 1
        return False
