class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return n
        desired = "A"*n
        cache = {}
        def dfs(x, clipBoard, count):
            if x == 0:
                return count
            if x < 0:
                return float('inf')
            # n is even and n > 2
            # 2 options every time copy existing or paste from clipboard
            len_cur = n-x
            return min( dfs(x-clipBoard, clipBoard, count+1), dfs(n-(2*len_cur), len_cur, count+2))
        return dfs(n-1,1,1)
