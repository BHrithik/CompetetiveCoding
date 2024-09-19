class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # res = []
        # def helper(left,right):
        #     sub_exp = expression[left:right+1]
        #     if '-' not in sub_exp and '+' not in sub_exp and '*' not in sub_exp:
        #         return int(sub_exp)
            


        operations = {
            '+':lambda x,y : x+y,
            '-':lambda x,y : x-y,
            '*':lambda x,y : x*y
        }
        def backtrack(left,right):
            sub_exp = expression[left:right+1]
            if '-' not in sub_exp and '+' not in sub_exp and '*' not in sub_exp:
                return [int(sub_exp)]
            res = []
            for i in range(left, right+1):
                if expression[i] in operations:
                    nums1 = backtrack(left,i-1)
                    nums2 = backtrack(i+1,right)
                    for n in nums1:
                        for n2 in nums2:
                            res.append(operations[expression[i]](n,n2))
            # if res == []:
            #     res.append(int(expression[left:right+1]))
            return res  
        return backtrack(0,len(expression)-1)