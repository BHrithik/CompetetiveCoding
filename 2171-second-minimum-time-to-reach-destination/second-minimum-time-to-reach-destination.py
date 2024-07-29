class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        times = [[float('inf')]*2 for _ in range(n+1)]
        times[1][0]=0
        queue = deque([(1,0)])
        while queue:
            cur_city, cur_time = queue.popleft()
            for neighbour in graph[cur_city]:
                new_time = cur_time + 1
                if times[neighbour][0] > new_time:
                    times[neighbour][1] = times[neighbour][0]
                    times[neighbour][0] = new_time
                    queue.append((neighbour, new_time))
                elif times[neighbour][0] < new_time < times[neighbour][1]:
                    times[neighbour][1] = new_time
                    queue.append((neighbour, new_time))
        second_shortest_path_length = times[n][1]
        total_time = 0
        for i in range(second_shortest_path_length):
            if (total_time//change)%2 == 1: # stop
                total_time = (total_time // change + 1) * change
            total_time += time
        return total_time

