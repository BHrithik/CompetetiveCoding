class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()
        ans = 0
        def dfs(city):
            connections = isConnected[city]
            connections[city] = 0
            visited.add(city)
            for i in range(N):
                if i not in visited and connections[i] == 1:
                    dfs(i)
            return

        for i in range(N):
            if i not in visited:
                dfs(i)
                ans = ans+1
        return ans