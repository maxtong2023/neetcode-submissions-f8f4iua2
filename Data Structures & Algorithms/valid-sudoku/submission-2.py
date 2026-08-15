class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for row in range(len( board)): 

            for col in range(len(board[0])): 
                digit = board[row][col]
                if digit == ".": 
                    continue
                else: 

                    rows[row] = rows.get(row, set())
                    if digit in rows[row]: 
                        return False
                    rows[row].add(digit)

                    cols[col] = cols.get(col, set())
                    if digit in cols[col]: 
                        return False
                    cols[col].add(digit)

                    boxrow = row // 3
                    boxcol = col // 3

                    boxIndex = boxrow * 3 + boxcol
                    boxes[boxIndex] = boxes.get(boxIndex, set())
                    if digit in boxes[boxIndex]: 
                        return False
                    boxes[boxIndex].add(digit)
        return True



                