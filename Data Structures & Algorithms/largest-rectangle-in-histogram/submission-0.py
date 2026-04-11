class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # think of starting from a bar in the middle and going left and right. 
        # you would not be able to extend the bar further left or right if 
        # the left or right bar is less than the height of the middle bar. 
        n = len(heights)
        stack = []
        maxarea = 0 

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j
                maxarea = max(maxarea, w*h)
                start = j
            stack.append((height, start))
        while stack: 
            h, j = stack.pop()
            w = n - j
            maxarea = max(maxarea, w*h)
        return maxarea