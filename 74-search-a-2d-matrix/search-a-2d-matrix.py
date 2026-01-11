class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            l = 0
            r = len(arr)-1
            while l <= r:
                m = (l+r) // 2
                if arr[m] == target:
                    return True
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        l_row = 0
        r_row = len(matrix)-1
        while l_row <= r_row:
            m_row = (l_row+r_row)//2
            if matrix[m_row][0] <= target <= matrix[m_row][-1]:
                return binary_search(matrix[m_row], target)
            if matrix[m_row][0] > target:
                r_row = m_row - 1
            else:
                l_row = m_row + 1
        return False
