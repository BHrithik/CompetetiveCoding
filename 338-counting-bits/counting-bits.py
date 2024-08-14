class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            arr.append(i.bit_count())
        return arr