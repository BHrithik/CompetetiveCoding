class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        sentences = []
        def dfs(index, path):
            if index == len(s):
                sentences.append(' '.join(path))
                return
            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordSet:
                    dfs(i, path + [s[index:i]]) 
        dfs(0, [])
        return sentences