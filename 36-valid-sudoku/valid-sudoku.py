class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        cols = defaultdict(set)
        rows = defaultdict(set)
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                box_n = ((i//3)*3,(j//3)*3)
                if board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in boxes[box_n]:
                    return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                boxes[box_n].add(board[i][j])
        return True
    