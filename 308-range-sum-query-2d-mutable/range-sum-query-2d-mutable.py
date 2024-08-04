class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.A = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.A[i][j] = matrix[i][j]
                if i > 0:
                    self.A[i][j] += self.A[i - 1][j]
                if j > 0:
                    self.A[i][j] += self.A[i][j - 1]
                if i > 0 and j > 0:
                    self.A[i][j] -= self.A[i - 1][j - 1]

    def update(self, row: int, col: int, val: int) -> None:
        diff = val -  self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(row, len(self.A)):
            for j in range(col, len(self.A[0])):
                self.A[i][j] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regSum = self.A[row2][col2]
        if row1 > 0:
            regSum -= self.A[row1-1][col2]
        if col1 > 0:
            regSum -= self.A[row2][col1-1]
        if row1 > 0 and col1 > 0:
            regSum += self.A[row1-1][col1-1]
        return regSum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)