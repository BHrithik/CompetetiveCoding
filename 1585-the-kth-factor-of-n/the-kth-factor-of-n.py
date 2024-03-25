class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        Farr = []
        for i in range(1,n+1):
            if n%i == 0:
                Farr.append(i)
        print(Farr)
        if k-1 >= len(Farr):
            return -1
        return Farr[k-1]