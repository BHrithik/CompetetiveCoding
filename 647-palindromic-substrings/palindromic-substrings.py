class Solution:
    def countSubstrings(self, s: str) -> int:
        pallindromes = 0
        def checkFromMiddle(l,r):
            count = 0
            while l >= 0 and r <= len(s)-1:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
            return count

        for i in range(len(s)):
            pallindromes += checkFromMiddle(i, i)  # the length is odd
            pallindromes += checkFromMiddle(i, i+1) # the length is odd
        return pallindromes



        # abcacba
        # a, b, c, a, cac, bcacb, abcacba, c, b, a length is odd
        # 














        # self.res = 0
        # def exploreFromMiddle(l,r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         self.res += 1
        #         l -= 1
        #         r += 1
        # for i in range(len(s)):
        #     exploreFromMiddle(i,i)
        #     exploreFromMiddle(i,i+1)
        # return self.res