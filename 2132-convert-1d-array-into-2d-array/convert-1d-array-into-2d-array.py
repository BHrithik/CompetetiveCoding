class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        res = [[0]*n for _ in range(m)]
        print(res)
        c = 0
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = original[c]
                c += 1
        print(res)
        return res