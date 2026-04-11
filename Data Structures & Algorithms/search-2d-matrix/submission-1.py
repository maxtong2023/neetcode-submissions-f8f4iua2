class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first check the last element of each row. If the target is greater than 
        # the element, move onto the next row. If it is less than, the number exists within 
        # that row. Do binary search to find the target within that row. 

        def search(row, target):
            left = 0
            right = len(row) - 1

            while left <= right: 
                middle = (left + right) // 2
                if row[middle] == target:
                    return True
                elif row[middle] > target: 
                    right = middle - 1
                else:
                    left = middle + 1
            return False

        rowlen = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][rowlen] == target: 
                return True
            if matrix[i][rowlen] > target: 
                return search(matrix[i], target)
        return False
                


         