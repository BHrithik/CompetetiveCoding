class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskDict = Counter(tasks)
        maxHeap = [-value for key,value in taskDict.items()]
        heapq.heapify(maxHeap)
        t = 0
        q = deque()
        while maxHeap or q:
            t += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count != 0:
                    q.append((count,t+n))
            if q and q[0][1] == t:
                count, _ = q.popleft()
                heapq.heappush(maxHeap,count)
        return t
