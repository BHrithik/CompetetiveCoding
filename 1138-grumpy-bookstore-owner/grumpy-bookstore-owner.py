class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        count = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                count += customers[i]
                customers[i] = 0
        max_satisfy = 0
        for i in range(0,len(customers)-minutes+1):
            max_satisfy = max(max_satisfy,sum(customers[i:i+minutes]))
        return max_satisfy + count