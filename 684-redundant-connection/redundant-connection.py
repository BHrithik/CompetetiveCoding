# Super undhi problem!

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return 1
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 0
        res = []
        for a,b in edges:
            if union(a-1,b-1) == 1:
                res.append([a,b])
        return res[-1]            
            
        