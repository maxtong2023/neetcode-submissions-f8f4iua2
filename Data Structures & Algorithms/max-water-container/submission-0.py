class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        maxarea = 0
        
        while right > left: 
            height = min(heights[left], heights[right])
            area = height * (right -left)
            maxarea = max(area, maxarea)

            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1
        return maxarea