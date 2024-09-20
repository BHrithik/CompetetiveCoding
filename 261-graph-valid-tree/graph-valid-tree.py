class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def helper(root, parent):
            if root == parent:
                return False
            if root in visited:
                return False
            visited.add(root)
            for nei in graph[root]:
                helper(nei,root)
            return True
        
        if not helper(0,-1):
            return False

        return len(visited) == n