class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = set()
        for i in matrix:
            k.update(set(i))
        return target in k