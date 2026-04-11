class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the array should have a cut where one element is less than the element after it. 
        right = len(nums) - 1
        left = 0 

        

        while left <= right: 
            mid = (right + left) // 2 

            if nums[mid] == target: 
                return mid
            if nums[left] <= nums[mid]: # left array is sorted
                if target >= nums[left] and target <= nums[mid]:
                    right = mid -1
                else: 
                    left = mid + 1
            else: #right array is sorted
                if target >= nums[mid] and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid - 1
        return -1


