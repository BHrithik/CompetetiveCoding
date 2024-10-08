class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        length = n*2
        res = []
        def helper(s, left, right):
            if len(s) == length:
                res.append(s)
                return
            if left < n:
                helper(s+"(", left+1,right)
            if right < left:
                helper(s+")", left, right+1)
        helper("",0,0)
        return res
        # length = n*2
        # res = set()
        # cache = defaultdict(list)
        # def helper(s,left,right):
        #     if len(s) == length and s not in res:
        #         res.add(s)
        #         return
        #     if left == right:
        #         cache[(left,right)] = s
        #         if (n-left,n-right) in cache:
        #             if s+cache[(n-left,n-right)] not in res:
        #                 res.add(s+cache[(n-left,n-right)])
        #                 print(f"{cache[(n-left,n-right)]} found in cache for {s}")
        #     if left < n:
        #         helper(s+"(",left+1, right)
        #     if right < left:
        #         helper(s+")",left,right+1)
        # helper("",0,0)
        # return list(res)