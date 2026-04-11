class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0 
        left = 0 
        right = len(height) - 1
        leftmax = 0 
        rightmax = 0 

        while left< right: 
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    total += leftmax - height[left]
                left +=1 
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    total += rightmax - height[right]
                right -=1 
        return total