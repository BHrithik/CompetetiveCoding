class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ["" for _ in range(numRows)]
        level = 0
        sign = 1
        for i in s:
            res[level] += i
            if level == numRows-1: # Going up once we reached the bottom
                sign = -1 # Going up
            if level == 0: # Going down once we reached the top
                sign = 1 # Going Down
            level += sign
        return "".join([i for i in res])