class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        for i,temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                pos = stack.pop()
                ans[pos] = i - pos
            stack.append(i)
        return ans