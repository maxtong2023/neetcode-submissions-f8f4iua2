class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find the cell in which the letter(s) are at
        # append all 4? potential candidates, and backtrack, and pop.
        # prune the word if it doesn't match. (maybe)
        # repeat until you are left with a word. If you don't get one, 
        # repeat the process with another starting point.
        vbound = len(board)
        hbound = len( board[0])
        def backtrack(row, col, index): 
            print(board[row][col])
            if board[row][col] != word[index]: 
                return False
            if index == len(word) - 1: 
                return True
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            temp = board[row][col]
            board[row][col] = "@"

            for dr, dc in directions: 
                newr = row + dr
                newc = col + dc
                if 0 <= newr < vbound and 0 <= newc < hbound and board[newr][newc] != "@":
                    if backtrack(newr, newc, index +1):
                        board[row][col] = temp
                        return True
            board[row][col] = temp
            return False
        
        for row in range(len(board)): 
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        return False







