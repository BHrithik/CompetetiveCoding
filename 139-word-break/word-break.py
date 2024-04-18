class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False]*(len(s)+1)
        ans[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (i+len(word)) <= len(s) and s[i:i+len(word)] == word:
                    ans[i] = ans[i+len(word)]
                if ans[i]:
                    break
        return ans[0]
                