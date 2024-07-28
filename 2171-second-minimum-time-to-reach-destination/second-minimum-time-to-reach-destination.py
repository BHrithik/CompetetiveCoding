from collections import defaultdict, deque
import heapq

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distances = [[float('inf')] * 2 for _ in range(n + 1)]
        distances[1][0] = 0
        queue = deque([(1, 0)])
        while queue:
            node, dist = queue.popleft()
            for neighbor in graph[node]:
                next_dist = dist + 1
                if next_dist < distances[neighbor][0]:
                    distances[neighbor][1] = distances[neighbor][0]
                    distances[neighbor][0] = next_dist
                    queue.append((neighbor, next_dist))
                elif distances[neighbor][0] < next_dist < distances[neighbor][1]:
                    distances[neighbor][1] = next_dist
                    queue.append((neighbor, next_dist))
        second_shortest_path_length = distances[n][1]
        total_time = 0
        for _ in range(second_shortest_path_length):
            if (total_time // change) % 2 == 1:  # Red light
                total_time = (total_time // change + 1) * change
            total_time += time
        return total_time