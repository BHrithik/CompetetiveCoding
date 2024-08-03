class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        arr = deque([])
        for i in range(0,n):            
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for i in range(0,n):
            matrix[i].reverse()
        