class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for city1, city2, w in edges:
            dist[city1][city2] = w
            dist[city2][city1] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]
        res = float('inf')
        bestCity = -1

        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachableCities += 1
            if reachableCities <= res:
                res = reachableCities
                bestCity = i
        return bestCity

        res = []
        def calculateNeighbours(city, distance):
            if distance <= 0:
                return []
            neighbours = []
            for city1,city2,weight in edges:
                if city == city1 and distance >= weight:
                    neighbours.append(city2)
                    neighbours.extend(calculateNeighbours(city2,distance-weight))
                elif city == city2 and distance >= weight:
                    neighbours.append(city1)
                    neighbours.extend(calculateNeighbours(city1,distance-weight))
            neighbours = [i for i in neighbours if i != city]
            return neighbours
        ans = float('inf')
        for i in range(n):
            num_neighbours = len(set(calculateNeighbours(i,distanceThreshold)))
            res.append((num_neighbours,-i))
        res.sort()
        return -res[0][1]

