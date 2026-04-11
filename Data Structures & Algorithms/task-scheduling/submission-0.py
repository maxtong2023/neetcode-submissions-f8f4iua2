import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # create a set of all the elements

        freqs = {}

        for i in tasks: 
            freqs[i] = freqs.get(i, 0) + 1
        

        # always try the task with the most frequencies first

        count = 0
        heap = []

        for i in freqs: 
            heapq.heappush(heap, -freqs[i])# frequency and letter
        # all tasks are available to begin with 

        time = 0 
        cooldown = deque()

        while heap or cooldown: 
            time += 1 

            if heap: 
                count = heapq.heappop(heap)
                count +=1 
                if count != 0:
                    cooldown.append((count, time + n))
            if cooldown:
                if cooldown[0][1] == time: 
                    heapq.heappush(heap, cooldown.popleft()[0])
                    
        return time




                
            
