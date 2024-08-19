class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return n
        res = float('inf')
        desired = "A"*n
        cache = {}
        def dfs(x, clipBoard, count):
            if x == desired:
                return count
            if len(x) > n:
                return float('inf')
            # n is even and n > 2
            # 2 options every time copy existing or paste from clipboard
            return min(dfs(x+clipBoard,clipBoard,count+1), dfs(x+x,x,count+2))
        return dfs("A","A",1)
