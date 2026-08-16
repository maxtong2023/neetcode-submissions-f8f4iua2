class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # is there any way to find from nums the particular numbers that have to be the leftmost element of any sequence? 

        # if i am the leftmost element, this must mean that my number - 1 does not exist in the set. 

        numset = set()
        for num in nums: 
            numset.add(num)
        
        # thus, the numbers in nums that are not in the set must be the beginnings of any sequence. 
        
        # when you iterate through, the worst it can be is linear. 
        best = 0
        for num in numset: 
            if num - 1 in numset: 
                # this means that it is not a start of a sequence
                continue
            else: 
                i = num
                count = 0 
                while i in numset: 
                    count += 1
                    best = max(best, count)
                    i += 1
        return best