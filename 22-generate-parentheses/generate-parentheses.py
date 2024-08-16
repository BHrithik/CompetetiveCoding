class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        length = n*2
        res = set()
        cache = defaultdict(list)
        def helper(s,left,right):
            if len(s) == length and s not in res:
                res.add(s)
            if left < n:
                helper(s+"(",left+1, right)
            if right < left:
                helper(s+")",left,right+1)
        helper("",0,0)
        return list(res)