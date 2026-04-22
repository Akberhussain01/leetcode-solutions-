class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        # fill sets and store empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    box = (i // 3) * 3 + (j // 3)
                    boxes[box].add(num)
        
        
        def solve(index):
            if index == len(empty):
                return True
            
            i, j = empty[index]
            box = (i // 3) * 3 + (j // 3)
            
            for num in "123456789":
                if num not in rows[i] and num not in cols[j] and num not in boxes[box]:
                    
                    # place
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)
                    
                    if solve(index + 1):
                        return True
                    
                    # backtrack
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box].remove(num)
            
            return False
        
        
        solve(0)
