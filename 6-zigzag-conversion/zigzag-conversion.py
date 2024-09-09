class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[""] for _ in range(numRows)]
        level = 0
        sign = 1
        for i in s:
            res[level][0] += i
            if level == numRows-1:
                sign = -1
            if level == 0:
                sign = 1
            level += sign
        return "".join([i[0] for i in res])