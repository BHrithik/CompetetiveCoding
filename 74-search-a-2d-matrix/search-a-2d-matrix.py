class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        row = 0
        while l <= r:
            m = (l+r)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif target < matrix[m][0]:
                r = m-1
            else:
                l = m+1
        arr = matrix[row]
        l = 0
        r = len(matrix[row]) -1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False