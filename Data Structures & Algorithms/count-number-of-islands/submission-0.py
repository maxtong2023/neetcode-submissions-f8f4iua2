class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        #DFS or BFS through the grid, marking it as 0 when you reach a node. 
        #
        islands = 0
        def dfs(r, c):
            stack = [(r, c)]

            while stack: 
                currentr, currentc = stack.pop()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in directions: 
                    newr = currentr + dr
                    newc = currentc + dc

                    if 0 <= newr <= len(grid) - 1 and 0 <= newc <= len(grid[0]) - 1 and grid[newr][newc] != "0":
                        grid[newr][newc] = "0"
                        stack.append((newr, newc))




        for row in range(len(grid)): 
            for col in range(len(grid[0])):
                if grid[row][col] == "1": 
                    dfs(row, col)
                    islands +=1
        return islands
