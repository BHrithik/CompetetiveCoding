class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num<0:
            num += 2 ** 32
        hexStr = ""
        hexDict = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f',
        }
        while num > 0:
            rem = num%16
            if rem < 10:
                hexStr = str(rem) + hexStr
            else:
                print(rem)
                hexStr = hexDict[rem] + hexStr 
            num = num//16
        return hexStr