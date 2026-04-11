import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # retain a min heap with length k?
        heap = []

        for num in nums:

            if len(heap)< k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]

            

        