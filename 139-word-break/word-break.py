class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(cur_s,rem_s):
            if rem_s in cache:
                return cache[rem_s]
            if len(cur_s) > len(s):
                return False
            if cur_s == s:
                return True
            res = False
            for i in wordDict:
                if rem_s[:len(i)] == i and len(cur_s)+len(i) <= len(s):
                    res = res or dfs(cur_s+i,rem_s[len(i):])
            cache[rem_s] = res
            return cache[rem_s]
        wordDict.sort(key=lambda x: len(s),reverse = True)
        return dfs("",s)
