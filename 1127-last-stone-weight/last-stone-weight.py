class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones] # gives us all negative weights 
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 == stone2:
                continue
            heapq.heappush(stones,-1*abs(stone1-stone2))
        return -1*stones[0] if stones else 0

