class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        routes = { (a,b) for a,b in connections}
        neighbours = defaultdict(list)
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        visited = set()
        count = 0
        def dfs(city):
            nonlocal count
            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if (neighbour,city) not in routes:
                    count += 1
                visited.add(city)
                dfs(neighbour)
        visited.add(0)
        dfs(0)
        return count
            