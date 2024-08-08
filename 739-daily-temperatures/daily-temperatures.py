class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                last_index,last_temp = stack.pop()
                res[last_index] = index-last_index
            stack.append([index,temp])
        return res

