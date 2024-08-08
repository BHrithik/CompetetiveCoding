class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pos = [[pos,speed] for pos,speed in zip(position,speed)]

        stack = []
        for pos,speed in sorted(car_pos,reverse=True):
            if stack and (target-stack[-1][0])/stack[-1][1] >= (target-pos)/speed:
                continue
            else:
                stack.append([pos,speed])
        return len(stack)