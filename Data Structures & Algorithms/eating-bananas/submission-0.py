class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        answer = right

        while left <= right: 
            middle = left + (right - left) // 2

            hours = 0 

            for pile in piles: 
                hours += (pile + middle - 1) // middle # ceiling division. 
            if hours <= h: 
                answer = middle
                right = middle - 1

            else:
                left = middle + 1
        return answer