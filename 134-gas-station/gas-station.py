class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cur_sum = 0
        start = 0
        for i in range(0,len(gas)):
            cur_sum += gas[i]-cost[i]
            if cur_sum < 0:
                cur_sum = 0
                start = i+1
        return start