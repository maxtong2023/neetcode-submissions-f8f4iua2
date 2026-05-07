class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        rowbound = len(grid) 
        colbound = len(grid[0])

        maxarea = 0

        def dfs(start):
            stack = [start]
            area = 1

            while stack:
                coordinates = stack.pop()
                if coordinates not in seen: 
                    seen.add(coordinates)
                row, col = coordinates
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                
                for dr, dc in directions: 
                    newr = row + dr
                    newc = col + dc
                    if newr < rowbound and newc < colbound and newr >= 0 and newc >=0 and grid[newr][newc] == 1:
                        
                        newcoord = (newr, newc)
                        if newcoord not in seen:
                            print(newcoord)
                            stack.append(newcoord)
                            seen.add(newcoord)
                            area += 1
            return area
            


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                coordinates = (row, col)

                if coordinates not in seen and grid[row][col] == 1: 
                    # start a new DFS. 
                    maxarea = max(maxarea, dfs(coordinates))
        return maxarea
        