class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            skip = False
            for n in range(len(target)):
                if t[n] > target[n]:
                    skip = True
            if not skip:
                for i in range(len(t)):
                    if t[i] == target[i]:
                        good.add(i)
        return len(good) == len(target)