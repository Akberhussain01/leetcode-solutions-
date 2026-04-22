class Solution:
    def isValidSudoku(self, board):
        rows = set()
        cols = set()
        boxes = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == ".":
                    continue
                
                row_key = (i, num)
                col_key = (j, num)
                box_key = (i // 3, j // 3, num)
                
                if row_key in rows or col_key in cols or box_key in boxes:
                    return False
                
                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)
        
        return True
