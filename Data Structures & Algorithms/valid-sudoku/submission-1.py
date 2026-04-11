class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # step 1: check for duplicates in each row

        for i in range(9):
            seen = set()
            for k in range(9):
                if board[i][k] == '.':
                    continue
                elif board[i][k] in seen: 
                    return False
                else: 
                    seen.add(board[i][k])
        # step 2: check for every column

        for i in range(9):
            seen = set()
            for k in range(9):
                if board[k][i] == '.':
                    continue
                elif board[k][i] in seen: 
                    return False
                else:
                    seen.add(board[k][i])
        # step 3: check for every square

        for i in range(0, 3):
            for k in range(0, 3):
                seen = set()
                for j in range(0, 3):
                    for z in range(3):
                        x = (k * 3) + z
                        y = (i * 3) + j
                        if board[x][y] == '.':
                            continue
                        elif board[x][y] in seen: 
                            return False
                        else:
                            seen.add(board[x][y])
        return True


