class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            flag = False
            for i in range(len(target)):
                if t[i] > target[i]:
                    flag = True
                    break
            if not flag:
                for i in range(len(target)):
                    if t[i] == target[i]:
                        good.add(i)
        return len(good) == 3
