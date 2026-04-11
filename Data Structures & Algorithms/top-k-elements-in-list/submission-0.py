from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count frequencies
        freq = {}

        for i in nums: 
            if(freq.get(i) == None):
                freq[i] = 1
            else:
                freq[i] = freq[i] + 1


        # Step 2: make buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: collect from high frequency down
        res = []
        for i in range(len(buckets) - 1, 0, -1):  # from high to low
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
