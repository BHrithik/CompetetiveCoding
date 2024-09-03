class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(0,minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        res = []
        visited = {}
        def dfs(c):
            if c in visited:
                if visited[c] == 1:
                    return True
                if visited[c] == 2:
                    return False
            visited[c] = 1
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = 2
            res.append(c)
            return False
        
        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])