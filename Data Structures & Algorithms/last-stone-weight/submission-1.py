class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        biggest = 0 
        smallest = 0 

        while len(stones) >= 2:
            biggest = max(stones)
            stones.remove(biggest)
            smallest = max(stones)
            stones.remove(smallest)

            y = biggest - smallest

            if(y != 0):
                stones.append(y)
        if(stones == []):
            return 0
        else:
            return stones[0]








            

            








            

            


            
        