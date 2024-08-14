class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        numDict = {
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        cur_s = []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(cur_s[:]))
                return
            for choice in numDict[digits[i]]:
                cur_s.append(choice)
                dfs(i+1)
                cur_s.pop()
        dfs(0)
        return res