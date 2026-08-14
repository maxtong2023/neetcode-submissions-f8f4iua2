class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        counts = {}
        for num in nums: 
            counts[num] = counts.get(num, 0) + 1 

        for key in counts: 
            buckets[counts[key]].append(key)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1): 
            for num in buckets[i]: 
                result.append(num)
                if len(result) == k: 
                    return result
        
        

        
