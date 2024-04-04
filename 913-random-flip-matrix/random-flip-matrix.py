class Solution:

    def __init__(self, m: int, n: int):
        self.used = set()
        self.m = m
        self.n = n
        

    def flip(self) -> List[int]:
        r = random.randint(0, (self.m*self.n)-1)
        while r in self.used:
            r = random.randint(0, (self.m*self.n)-1)
        self.used.add(r)
        return [r//self.n,r%self.n]

    def reset(self) -> None:
        self.used = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()