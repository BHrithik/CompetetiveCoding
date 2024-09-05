class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(lambda: set())
        rows = defaultdict(lambda: set())
        boxes = defaultdict(lambda: set())
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                box = ((i//3)*3, (j//3)*3) # To caculate which box the current number lies in 
                if board[i][j] in cols[i] or board[i][j] in rows[j] or board[i][j] in boxes[box]:
                    return False
                cols[i].add(board[i][j])
                rows[j].add(board[i][j])
                boxes[box].add(board[i][j])
        return True
                
