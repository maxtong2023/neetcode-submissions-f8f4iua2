import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points: 
            distance = math.sqrt(point[0]**2 + point[1]**2)

            if len(heap) < k:
                heapq.heappush_max(heap, (distance, point))
            elif distance < heap[0][0]: # the first tuple's first element is the distance
                heapq.heappop(heap)
                heapq.heappush_max(heap, (distance, point))
        
        return [point for dist, point in heap]
