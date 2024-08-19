class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        cache = {}
        
        def dfs(x, clipBoard, count):
            if x == 0:
                return count
            if x < 0:
                return float('inf')
            
            # Use a tuple of (x, clipBoard) as the cache key
            if (x, clipBoard) in cache:
                return cache[(x, clipBoard)] + count
            
            len_cur = n - x
            
            # Calculate both options: paste or copy-paste
            result = min(
                dfs(x - clipBoard, clipBoard, count + 1),  # Paste from clipboard
                dfs(n - (2 * len_cur), len_cur, count + 2)  # Copy All + Paste
            )
            
            # Store the result in the cache before returning
            cache[(x, clipBoard)] = result - count
            return result
        
        return dfs(n - 1, 1, 1)
