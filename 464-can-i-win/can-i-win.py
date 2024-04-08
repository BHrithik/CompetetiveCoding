class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 1:
            return True
        if (maxChoosableInteger*(maxChoosableInteger+1))/2 < desiredTotal:
            return False
        memo = {}
        def canWin(choices, amount):
            if choices and choices[-1] >= amount:
                return True
            if choices in memo:
                return memo[choices]
            for i in range(len(choices)):
                if not canWin(choices[:i]+choices[i+1:],amount-choices[i]):
                    memo[choices] = True
                    return True
            memo[choices] = False
            return False
        return canWin(tuple(range(1,maxChoosableInteger+1)), desiredTotal)
