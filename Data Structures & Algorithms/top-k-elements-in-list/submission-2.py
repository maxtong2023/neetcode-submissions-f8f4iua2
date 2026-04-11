class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        maximum = 0  
        freqs = {}
        for i in nums: 
            freqs[i] = freqs.get(i, 0) + 1
            maximum = max(maximum, freqs[i])
        
        # create the buckets
        buckets = [[] for _ in range(maximum)]
        # somehow this is different from buckets = [[]] * maximum

        for i in freqs: 
            buckets[freqs[i] - 1].append(i)
        result = []
        index = len(buckets) - 1
        while len(result) < k:
            if len(buckets[index]) == 0:
                index -= 1
                continue
            for i in buckets[index]:
                result.append(i)
                if len(result) == k:
                    return result
            index -= 1
        

        