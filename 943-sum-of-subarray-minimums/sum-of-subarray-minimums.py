class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Mod = 10**9 + 7
        res = 0
        arr = [float('-inf')]+arr+[float('-inf')]
        stack = []
        # Iterate over all possible starting indices
        for i,n  in enumerate(arr):
            while stack and n < stack[-1][1]:
                j,prev_min = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + left * right * prev_min) % Mod
            stack.append((i,n))
        return res
