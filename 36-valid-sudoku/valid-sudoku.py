class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkInBox(i,j):
            if i < 3 and j < 3:
                p1 = (0,0)
            elif i < 3 and j < 6:
                p1 = (0,3)
            elif i < 3 and j < 9:
                p1 = (0,6)
            elif i < 6 and j < 3:
                p1 = (3,0)
            elif i < 6 and j < 6:
                p1 = (3,3)
            elif i < 6 and j < 9:
                p1 = (3,6)
            elif i < 9 and j < 3:
                p1 = (6,0)
            elif i < 9 and j < 6:
                p1 = (6,3)
            else:
                p1 = (6,6)
            for x in range(p1[0],p1[0]+3):
                for y in range(p1[1],p1[1]+3):
                    if (x,y) != (i,j) and board[i][j] == board[x][y]:
                        return False
            return True

        def validate(i,j):
            actual_val = board[i][j]
            for x in range(n):
                if x!= i and actual_val == board[x][j]: #All in the same column
                    return False
                if x!= j and actual_val == board[i][x]: #All in the same row
                    return False
            return checkInBox(i,j)

        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != "." and not validate(i,j):
                    return False
        return True
    