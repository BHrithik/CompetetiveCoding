class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # check long substring from middle as i
            l = i
            r = i
            # assuming longest pallindrome is odd
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            if i+1 < len(s) and s[i+1] == s[i]:
                # assuming longest pallidrome is even
                l = i
                r = i+1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        if r-l+1 > len(res):
                            res = s[l:r+1]
                        l -= 1
                        r += 1
                    else:
                        break
        return res








        # self.res = ""
        # self.max_len = 0
        # def fromMiddle(l,r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if r-l+1 > self.max_len:
        #             self.max_len = r-l+1
        #             self.res = s[l:r+1]
        #         l -= 1
        #         r += 1
        # for i in range(0,len(s)):
        #     fromMiddle(i,i)
        #     fromMiddle(i,i+1) 
        # return self.res