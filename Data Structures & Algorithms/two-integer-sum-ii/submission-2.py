class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0 
        result = 0

        while left < right: 
            result = numbers[left] + numbers[right]
            if result == target: 
                return [left + 1, right + 1]
            elif result < target: 
                left +=1 
            else: 
                right -=1
