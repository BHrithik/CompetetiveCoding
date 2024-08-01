class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}
        def helper(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = float('inf')
            curWidth = shelfWidth
            maxHeight = 0
            for j in range(i,len(books)):
                width, height = books[j]
                if width > curWidth:
                    break
                curWidth -= width
                maxHeight = max(maxHeight, height)
                cache[i] = min(helper(j+1)+maxHeight,cache[i])
            return cache[i]
        return helper(0)