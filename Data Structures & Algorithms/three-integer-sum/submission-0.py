class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1  # Start after i, not at 0
            right = len(nums) - 1
            target = -nums[i]
            
            while right > left:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif current_sum < target:
                    left += 1  # Need larger sum
                else:
                    right -= 1  # Need smaller sum
        
        return result