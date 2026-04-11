class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # step 1: find out which elements are the start of a sequence. 
        freq = set()
        for i in nums: 
            freq.add(i)
        starters = []
        for i in freq: 
            if i -1 not in freq:
                starters.append(i)
        maxlen = 0
        for i in starters: 
            index = i
            length = 0
            while index in freq: 
                index +=1 
                length += 1
                maxlen = max(maxlen, length)
            length = 0

        return maxlen

