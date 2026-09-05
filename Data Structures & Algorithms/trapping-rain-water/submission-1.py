class Solution:
    def trap(self, height: List[int]) -> int:
        leftarray = []
        rightarray = []

        right = len(height) - 1
        left = 0
        leftmax = 0
        rightmax = 0
        for i in range(len(height)): 
            leftarray.append(leftmax)
            rightarray.append(rightmax)
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            left +=1 
            right -=1
        rightarray = rightarray[::-1]
        total = 0
        for i in range(len(height)): 
            water = max(0, min(leftarray[i], rightarray[i]) - height[i])
            total += water
        return total
            