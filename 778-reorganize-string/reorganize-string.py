class Solution:
    def reorganizeString(self, s: str) -> str:
        dicc = Counter(s)
        maxHeap = [ [-cnt, char] for char,cnt in dicc.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt,char = heapq.heappop(maxHeap)
            res = res + char
            cnt = cnt + 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
            
        return res