class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pos = [[pos,speed] for pos,speed in zip(position,speed)]

        stack = []
        for pos,speed in sorted(car_pos,reverse=True):
            stack.append((target-pos)/speed)
            if len(stack) >=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)