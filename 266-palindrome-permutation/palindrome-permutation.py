class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = Counter(s)
        flag = True
        for i in d.keys():
            if d[i]%2 == 0:
                continue
            if d[i]%2 != 0 and flag:
                flag = False
            else:
                return False
        return True