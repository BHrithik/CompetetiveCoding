class Solution:
    def countBits(self, n: int) -> List[int]:
        def binary(a):
            s = ''
            while a:
                s = str(a%2) + s
                a = a//2
            return s
        ans = [0]
        for i in range(1,n+1):
            bitDict = Counter(binary(i))
            print(bitDict)
            print(bitDict['1'])
            ans.append(bitDict['1'])
        return ans