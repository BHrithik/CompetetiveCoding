class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        task_counter = Counter(tasks)
        max_heap = [-val for key, val in task_counter.items()]
        heapq.heapify(max_heap)
        print(max_heap)
        rem_q = deque([])
        time = 0
        while len(max_heap) > 0 or len(rem_q) > 0:
            if max_heap:
                task_to_process = heapq.heappop(max_heap)
                task_to_process += 1
                if task_to_process < 0:
                    rem_q.append((task_to_process,time+n))
            while rem_q and rem_q[0][1] <= time:
                task,_ = rem_q.popleft()
                heapq.heappush(max_heap,task)
            time += 1
        return time