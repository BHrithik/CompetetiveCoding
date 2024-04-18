class Solution:
    def romanToInt(self, s: str) -> int:
        ans = []
        if 'IV' in s:
            s=s.replace('IV','4,')
        if 'IX' in s:
            s=s.replace('IX','9,')
        if 'XL' in s:
            s=s.replace('XL','40,')
        if 'XC' in s:
            s=s.replace('XC','90,')
        if 'CD' in s:
            s=s.replace('CD','400,')
        if 'CM' in s:
            s=s.replace('CM','900,')
        if 'I' in s:
            s=s.replace('I','1,')
        if 'V' in s:
            s=s.replace('V','5,')
        if 'X' in s:
            s=s.replace('X','10,')
        if 'L' in s:
            s=s.replace('L','50,')
        if 'C' in s:
            s=s.replace('C','100,')
        if 'D' in s:
            s=s.replace('D','500,')
        if 'M' in s:
            s=s.replace('M','1000,')
        print(s)
        ans = 0
        nums=s.split(',')
        for i in nums:
            if i:
                ans = ans + int(i)
        return ans