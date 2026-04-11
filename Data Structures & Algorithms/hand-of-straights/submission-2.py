import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = {}

        for i in hand: 
            counts[i] = counts.get(i, 0 )+1
        min_heap = list(counts)
        
        heapq.heapify(min_heap)
        
        while min_heap:
            smallest = min_heap[0] # Look at the smallest card
            
            # If this card's count is 0, we've already used it in a previous group
            if counts[smallest] == 0:
                heapq.heappop(min_heap)
                continue
                
            # Try to form a group starting from 'smallest'
            for i in range(smallest, smallest + groupSize):
                if counts.get(i) == 0 or counts.get(i) == None:
                    return False
                counts[i] -= 1
                
        return True