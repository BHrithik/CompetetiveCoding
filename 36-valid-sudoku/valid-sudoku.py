class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(i,j):
            for x in range(n):
                if x!= i and board[i][j] == board[x][j]: #All in the same column
                    return False
                if x!= j and board[i][j] == board[i][x]: #All in the same row
                    return False
            p1 = (i//3*3,j//3*3) # Caclulate start point of box
            for x in range(p1[0],p1[0]+3):
                for y in range(p1[1],p1[1]+3):
                    if (x,y) != (i,j) and board[i][j] == board[x][y]:
                        return False
            return True
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != "." and not validate(i,j):
                    return False
        return True
    