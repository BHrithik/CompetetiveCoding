class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missingSum = (mean*(m+n))-sum(rolls)
        res = []
        if missingSum < n or missingSum > 6*n:
            return res
        while n:
            dice= min(6, missingSum-n+1)
            res.append(dice)
            missingSum -= dice
            n -= 1
        return res