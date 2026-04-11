import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []

        for i in nums: 
            heapq.heappush(self.nums, i) # retain a max heap

        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        return min(heapq.nlargest(self.k, self.nums))
        
