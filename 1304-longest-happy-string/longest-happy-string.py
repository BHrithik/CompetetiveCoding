class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = "#"
        count = Counter({'a':a, 'b':b, 'c':c})
        # chars = sorted(count.values(),key=lambda x: count[x])
        while count:
            (a1, _),(a2, _) = count.most_common(2)
            if len(res) > 2 and res[-1] == res[-2] == a1:
                a1 = a2
            if not count[a1]:
                break
            res+= a1
            count[a1] -= 1
        return res[1:]