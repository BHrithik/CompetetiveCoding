class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        for i,temp in enumerate(temps):
            while stack and stack[-1][1] < temp:
                pos, _ = stack.pop()
                ans[pos] = i - pos
            stack.append([i, temp])
        return ans