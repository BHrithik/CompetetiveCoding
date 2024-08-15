class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billDict = defaultdict(int)
        for bill in bills:
            if bill == 5:
                billDict[bill] += 1
            if bill == 10:
                if billDict[5] > 0:
                    billDict[5] -= 1
                    billDict[10] += 1
                else:
                    return False
            if bill == 20:
                if billDict[10] > 0 and billDict[5] > 0:
                    billDict[10] -= 1
                    billDict[5] -= 1
                elif billDict[5] > 2:
                    billDict[5] -= 3
                else:
                    return False
        return True