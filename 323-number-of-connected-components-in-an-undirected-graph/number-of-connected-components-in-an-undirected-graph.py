class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphDict = {i:[] for i in range(n)}
        for a,b in edges:
            graphDict[a].append(b)
            graphDict[b].append(a)

        visited = set()
        def dfs(root):
            if root in visited or not graphDict[root]:
                return True
            visited.add(root)
            for nei in graphDict[root]:
                dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                print(visited)
                res += 1
        return res