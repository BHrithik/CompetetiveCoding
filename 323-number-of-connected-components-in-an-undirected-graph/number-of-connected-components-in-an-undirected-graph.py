class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphDict = {i:[] for i in range(n)}
        for a,b in edges:
            graphDict[a].append(b)
            graphDict[b].append(a)

        visited = set()
        def dfs(root):
            if root in visited or not graphDict[root]:
                return
            visited.add(root)
            for nei in graphDict[root]:
                dfs(nei)
        res = 0
        # res_compos = [set()]
        for i in range(n):
            if i not in visited:
                dfs(i)
                # res_compos.append(visited-res_compos[-1])
                res += 1
        # print(res_compos)
        return res