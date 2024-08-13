class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i>= len(s):
                res.append(part.copy())
                return
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    part.append(s[i:j])
                    dfs(j)
                    part.pop()
        dfs(0)
        return res
